import json


from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotAllowed, HttpResponseServerError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import timezone

from django.core import serializers

from doc_forum.forum.forms import Topic_Form, Topic_Update, Topic_Save, Forum_Form, Forum_Save, LikeChatForm
from doc_forum.forum.models import Topic, Forum, ForumLike
from doc_forum.doctos.models import Document
from doc_forum.fmail.models import SendFmail
from doc_forum.fmail.views import save_fmail, build_token_f, locate_object_f


@login_required(login_url='/manager/ingresar')
def forum_web(request):
    topics = Topic.objects.all()
    return render_to_response('topics_index.html',{'topics':topics, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
# @permission_required('institution.add_institution')
def upload_topic(request):
    if request.method=='POST':
        comment = request.POST.get('comment', False)
        title = request.POST.get('title', False)
        user_id = 1000
        if request.user.is_authenticated():
            user_id = request.user.id
            now = timezone.now()
            formulario = Topic_Save({'user': user_id, 'title': title, 'comment': comment, 'creation_date': now,'is_globally_pinned': 1}, request.FILES)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect(reverse("forum_web"))
    else:
        formulario = Topic_Form()
    return render_to_response('topic_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
# @permission_required('institution.change_institution')
def update_topic(request, id_topic):
    if id_topic:
        obj = get_object_or_404(Topic, id=id_topic)
        user_id = 1000
        if request.user.is_authenticated():
            user_id = request.user.id
            now = timezone.now()
            if obj:
                formulario = Topic_Form(request.POST or None, instance=obj)
                if request.method == 'POST':
                    comment = request.POST.get('comment', False)
                    title = request.POST.get('title', False)
                    if formulario.is_valid():
                        formulario.save()
                        return HttpResponseRedirect(reverse("forum_web"))
    return render_to_response('topic_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

def view_topic(request, id_topic):
    try:
        fmail = None
        if request.user.is_authenticated():
            fmail = SendFmail.objects.filter(topic=id_topic).filter(status=1).filter(user_owner=request.user.id)
        topic = get_object_or_404(Topic, id=id_topic)
        forum = Forum.objects.filter(topic=id_topic).order_by('creation_date')
        likes = ForumLike.objects.all().order_by('id')
        if request.method=='POST':
            comment = request.POST.get('comment', False)
            user_id = 1000
            if request.user.is_authenticated():
                user_id = request.user.id
                now = timezone.now()
                formulario = Forum_Save({'user': user_id, 'topic': id_topic, 'comment': comment, 'comment_html':comment,'creation_date': now}, request.FILES)
                if formulario.is_valid():
                    formulario.save()
                    #send mails
                    if request.user.is_authenticated():
                        fmails = SendFmail.objects.filter(topic=id_topic).filter(status=1)
                        if fmails:
                            for f in fmails:
                                if f.user_owner.id != request.user.id:
                                    is_authorized_string = "FORUM"
                                    save_fmail(locate_object_f(is_authorized_string, id_topic), is_authorized_string, f.user_owner.id, build_token_f(id_topic), f.id)
                    return HttpResponseRedirect(id_topic)
        else:
            formulario = Forum_Form()
        return render_to_response('topic_detail.html',{'forum':forum, 'topic':topic, 'fmail':fmail,'formulario':formulario, 'likes':likes}, context_instance=RequestContext(request))
    except SendFmail.DoesNotExist:
        print("Error No existe el objeto")
        return render_to_response('topic_detail.html',{'forum':forum, 'topic':topic, 'fmail':fmail,'formulario':formulario, 'likes':likes}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
# @permission_required('institution.change_institution')
def update_forum(request, id_forum, id_topic):
    if id_forum:
        obj = get_object_or_404(Forum, id=id_forum)
        user_id = 1000
        if request.user.is_authenticated():
            user_id = request.user.id
            now = timezone.now()
            if obj:
                formulario = Forum_Form(request.POST or None, instance=obj)
                if request.method == 'POST':
                    if formulario.is_valid():
                        formulario.save()
                        return HttpResponseRedirect(reverse("forum_web"))

    return render_to_response('topic_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

def delete_forum(request, id_forum, id_topic):
    forum = get_object_or_404(Forum, id=id_forum)
    if request.method == 'GET':
        forum.delete()
        return HttpResponseRedirect(reverse("view_topic", kwargs={'id_topic':id_topic}))
    else:
        return HttpResponse("Not allowed", status=403)

def save_like_forum(request):
    if request.is_ajax():
        try:
            data_list = []
            query_data = json.loads(request.POST['query_data'])
            forum=query_data['id_forum']
            user_id = 1000
            if request.user.is_authenticated():
                user_id = request.user.id
                now = timezone.now()
                forum_chat = ForumLike.objects.filter(user=user_id).filter(forum=forum)
                if forum_chat:
                    data_list.append(False)
                else:
                    like_form = LikeChatForm({'is_like':1,'user':user_id,'forum':forum,'creation_date':now})
                    if like_form.is_valid():
                        like_form.save()
                        data_list.append(True)
                return HttpResponse( json.dumps(data_list), content_type='application/json' )
        except Profile.DoesNotExist:
            print("Error No existe el objeto")
            return HttpResponse( json.dumps(data_list), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

def close_topic(request):
    if request.is_ajax():
        try:
            data_list = []
            query_data = json.loads(request.POST['query_data'])
            id_topic=query_data['id_topic']
            is_closed=query_data['is_closed']
            user_id = 1000
            if request.user.is_authenticated():
                user_id = request.user.id
                now = timezone.now()
                obj = get_object_or_404(Topic, id=id_topic)
                if obj:
                    if obj.is_closed:
                        obj.is_closed=0
                        obj.save()
                    else:
                        obj.is_closed=1
                        obj.save()
                    return HttpResponse( json.dumps(data_list), content_type='application/json' )
        except Topic.DoesNotExist:
            print("Error No existe el objeto")
            return HttpResponse( json.dumps(data_list), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
@permission_required('appointment.delete_topic')
def delete_topic(request, id_topic, template='topic_remove.html'):
    try:
        doc = get_object_or_404(Topic, id=id_topic)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "doc": doc
            }))
        if request.method == 'POST':
            doc.delete()
            return HttpResponseRedirect(reverse("forum_web"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this home_page',
            mimetype="text/plain",
            status=401
        )
