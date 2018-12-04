# -*- encoding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse

from datetime import datetime, timedelta, time
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core import serializers

from doc_forum.doctos.models import Document
from doc_forum.appointment.models import Event
from .forms import User_Basic_Update, User_Change_Password, MyUserCreationForm
from doc_forum.fmail.models import SendFmail
# from django.contrib.auth.views import password_change

@login_required(login_url='/manager/ingresar')
def agreement_and_proposal(request):
    appointments = None
    next_appointments = None
    now = timezone.now()
    d=datetime(now.year,now.month,now.day-1)
    end_date = Event.objects.filter(is_finally=0).order_by('-start_date')[:1]
    if end_date:
        for e in end_date:
            older = e.start_date
        appointments = Event.objects.filter(start_date__range=[now, older]).filter(is_finally=0).order_by('start_date')[:16]
    # start_events = Event.objects.all().order_by('start_date')[:1]
    # if start_events:
    #     for e in start_events:
    #         first_borin = e.start_date
        # next_appointments = Event.objects.all().filter(start_date__range=[first_borin, d]).all().order_by('start_date')
    next_appointments = Event.objects.all()
    docs = Document.objects.all()
    doc_dimension_1 = Document.objects.filter(dimension='1')
    doc_dimension_2 = Document.objects.filter(dimension='2')
    doc_dimension_3 = Document.objects.filter(dimension='3')
    doc_dimension_4 = Document.objects.filter(dimension='4')
    doc_dimension_5 = Document.objects.filter(dimension='5')
    doc_dimension_6 = Document.objects.filter(dimension='6')
    doc_dimension_7 = Document.objects.filter(dimension='7')
    doc_dimension_8 = Document.objects.filter(dimension='8')

    fmail = None
    if request.user.is_authenticated():
        fmail_1 = SendFmail.objects.filter(dimension=1).filter(status=1).filter(user_owner=request.user.id)
        fmail_2 = SendFmail.objects.filter(dimension=2).filter(status=1).filter(user_owner=request.user.id)
        fmail_3 = SendFmail.objects.filter(dimension=3).filter(status=1).filter(user_owner=request.user.id)
        fmail_4 = SendFmail.objects.filter(dimension=4).filter(status=1).filter(user_owner=request.user.id)
        fmail_5 = SendFmail.objects.filter(dimension=5).filter(status=1).filter(user_owner=request.user.id)
        fmail_6 = SendFmail.objects.filter(dimension=6).filter(status=1).filter(user_owner=request.user.id)
        fmail_7 = SendFmail.objects.filter(dimension=7).filter(status=1).filter(user_owner=request.user.id)
        fmail_8 = SendFmail.objects.filter(dimension=8).filter(status=1).filter(user_owner=request.user.id)
    return render_to_response('index.html',{'agre':docs,'doc_dimension_1':doc_dimension_1,'doc_dimension_2':doc_dimension_2,'doc_dimension_3':doc_dimension_3,'doc_dimension_4':doc_dimension_4
                                            ,'doc_dimension_8':doc_dimension_8,'doc_dimension_5':doc_dimension_5,'doc_dimension_6':doc_dimension_6,'doc_dimension_7':doc_dimension_7
                                            ,'fmail_1':fmail_1,'fmail_2':fmail_2,'fmail_3':fmail_3,'fmail_4':fmail_4
                                            ,'fmail_5':fmail_5,'fmail_6':fmail_6,'fmail_7':fmail_7,'fmail_8':fmail_8
                                            ,'appointments':appointments, 'next_appointments':next_appointments, 'now':d
                                            , 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

def home_page(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/manager/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    here = request.GET.get('next', '')
                    return HttpResponseRedirect('../..'+here)
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@permission_required('is_staff')
def nuevo_usuario(request):
    if request.method=='POST':
        formulario = MyUserCreationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            try:
                user = User.objects.get(username=usuario)
            except User.DoesNotExist:
                group_id = request.POST['group'];
                user_save = formulario.save()
                g = Group.objects.get(id=group_id)
                g.user_set.add(user_save.pk)
                return HttpResponseRedirect('/manager/usuario/list')
    else:
        formulario = MyUserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/manager/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    here = request.GET.get('next', '')
                    return HttpResponseRedirect('../..'+here)
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/manager/ingresar')
def user_list(request):
    users = User.objects.all().order_by("first_name")
    return render_to_response('user_list.html',{'items':users, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def user_detail(request, id_user):
    fmail = None
    if request.user.is_authenticated():
        fmail = SendFmail.objects.filter(user_follow=id_user).filter(status=1).filter(user_owner=request.user.id)
    user = get_object_or_404(User, pk=id_user)
    return render_to_response('user_detail.html',{'fmail':fmail,'us':user, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def user_delete(request, id_user):
    user = get_object_or_404(User, pk=id_user)
    user.delete()
    users = User.objects.all()
    return render_to_response('user_list.html',{'items':users}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('manager.change_user')
def user_update(request, id_user):
    id_user_loged = request.user.id
    # if str(id_user) in str(id_user_loged):
    obj = get_object_or_404(User, id=id_user)
    formulario = UserChangeForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../detail/'+ id_user)
    return render_to_response('user_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def user_update_basic(request, id_user):
    id_user_loged = request.user.id
    formulario = None
    if int(id_user) == int(id_user_loged):
        obj = get_object_or_404(User, id=id_user)
        formulario = User_Basic_Update(request.POST or None, instance=obj)
        if request.method == 'POST':
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect('../detail/'+ id_user)
    return render_to_response('user_basic_form.html',{'formulario':formulario, 'id_user':id_user}, context_instance=RequestContext(request))#, 'change_password': change_password}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def change_password(request):
    id_user_loged = request.user.id
    #if int(id_user) == int(id_user_loged):
    obj = get_object_or_404(User, id=id_user_loged)
    formulario = User_Change_Password(request.POST or None)
    if request.method == 'POST':
        if formulario.is_valid():
            password_old = request.POST['old_password'];
            password_new = request.POST['password'];
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(password_new)
            u.save()
            return HttpResponseRedirect('../detail/'+ str(request.user.id))
    return render_to_response('password_change_form.html',{'formulario':formulario}, context_instance=RequestContext(request))
