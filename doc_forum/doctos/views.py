# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied

from doc_forum.agreementgesp.models import Agreementgs

from .forms import Docto_Form,Docto_Form_With_Proposal, Docto_Update
from .models import Document
from doc_forum.proposal.models import Proposal
from doc_forum.agreement.models import Agreeement
from django.contrib.sites.models import Site
from doc_forum.fmail.models import SendFmail
from doc_forum.fmail.views import save_fmail, locate_object_f, build_token_docto

@login_required(login_url='/manager/ingresar')
@permission_required('doctos.add_document')
def upload_document(request):
    if request.method=='POST':
        title = request.POST.get('title', False)
        dimension = request.POST.get('dimension', False)
        objetive = request.POST.get('objetive', False)
        url = request.POST.get('url', False)
        author = request.POST.get('author', False)
        description = request.POST.get('description', False)
        user = request.POST.get('user', False)
        creation_date = request.POST.get('creation_date', False)
        if user == False:
            user = request.user.id
        formulario = Docto_Update({'title': title, 'dimension':dimension, 'objetive':objetive,'url':url, 'author':author, 'description':description, 'user':user, 'creation_date':creation_date}, request.FILES)
        if formulario.is_valid():
            obj_save = formulario.save()
            fmail = SendFmail.objects.filter(status=1).filter(user_follow=user)
            if fmail:
                for f in fmail:
                    is_authorized_string = "USER"
                    save_fmail(locate_object_f(is_authorized_string, user), is_authorized_string, f.user_owner.id, build_token_docto(obj_save.id), f.id)
            fmail_1 = SendFmail.objects.filter(status=1).filter(dimension=1)
            fmail_2 = SendFmail.objects.filter(status=1).filter(dimension=2)
            fmail_3 = SendFmail.objects.filter(status=1).filter(dimension=3)
            fmail_4 = SendFmail.objects.filter(status=1).filter(dimension=4)
            fmail_5 = SendFmail.objects.filter(status=1).filter(dimension=5)
            fmail_6 = SendFmail.objects.filter(status=1).filter(dimension=6)
            fmail_7 = SendFmail.objects.filter(status=1).filter(dimension=7)
            fmail_8 = SendFmail.objects.filter(status=1).filter(dimension=8)
            if fmail_1:
                send_dimension(fmail_1, user, obj_save, dimension)
            if fmail_2:
                send_dimension(fmail_2, user, obj_save, dimension)
            if fmail_3:
                send_dimension(fmail_3, user, obj_save, dimension)
            if fmail_4:
                send_dimension(fmail_4, user, obj_save, dimension)
            if fmail_5:
                send_dimension(fmail_5, user, obj_save, dimension)
            if fmail_6:
                send_dimension(fmail_6, user, obj_save, dimension)
            if fmail_7:
                send_dimension(fmail_7, user, obj_save, dimension)
            if fmail_8:
                send_dimension(fmail_8, user, obj_save, dimension)
            return HttpResponseRedirect(reverse("list_agreementgesp"))
    else:
        formulario = Docto_Form()
    return render_to_response('document_form.html',{'formulario':formulario, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('doctos.add_document')
def upload_docto_proposal(request, id_proposal):
    if request.method=='POST':
        if request.user.is_authenticated():
            user_id = request.user.id
            pro = get_object_or_404(Proposal, pk=id_proposal)
            formulario = Docto_Form_With_Proposal(request.POST, request.FILES)#({'title':title,'proposal':proposal,'docto_pro':doc})
            if formulario.is_valid():
                instance = Document(title=request.POST.get("title", ""),proposal=pro,docto_pro=request.FILES['docto_pro'])
                instance.save()
                return HttpResponseRedirect('../../proposal/'+id_proposal)
    else:
        formulario = Docto_Form_With_Proposal()
    return render_to_response('add_docto_proposal.html',{'formulario':formulario,'id_proposal':id_proposal}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('doctos.add_document')
def upload_docto_agreement(request, id_agreement):
    if request.method=='POST':
        agre = get_object_or_404(Agreementgs, pk=id_agreement)
        formulario = Docto_Form_With_Proposal(request.POST, request.FILES)
        if formulario.is_valid():
            instance = Document(title=request.POST.get("title", ""),agreementgs=agre,docto_pro=request.FILES['docto_pro'])
            instance.save()
            return HttpResponseRedirect('../../agreementgesp/'+id_agreement)
    else:
        formulario = Docto_Form_With_Proposal()
    return render_to_response('add_docto_proposal.html',{'formulario':formulario,'id_proposal':id_agreement}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('doctos.delete_document')
def delete_docto(request, id_docto, template='docto_remove.html'):
    try:
        doc = get_object_or_404(Document, id=id_docto)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "doc": doc
            }))
        if request.method == 'POST':
            doc.delete()
            return HttpResponseRedirect(reverse("list_agreementgesp"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this list_agreementgesp',
            mimetype="text/plain",
            status=401
        )
"""
This method is for multi mail dimension.
"""
def send_dimension(fmail, user, obj_save, dimension):
    if fmail:
        for f in fmail:
            if f.user_owner.id != user:
                if f.dimension in dimension:
                    is_authorized_string = "DIMENSION"
                    save_fmail(locate_object_f(is_authorized_string, dimension), is_authorized_string, f.user_owner.id, build_token_docto(obj_save.id), f.id)
