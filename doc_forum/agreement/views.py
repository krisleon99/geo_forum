from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models import Q
import json
from doc_forum.manager.excel_utils import WriteToExcel
from datetime import date, time
from datetime import datetime

from django.contrib.sites.models import Site

from .models import Agreeement, getValid, getAll, getInValid
from .forms import AgreementsForm, AgreementsUpdate
from doc_forum.doctos.models import Document

@login_required(login_url='/manager/ingresar')
def detail_agreement(request, id_agreement):
    formato = "%d/%m/%Y"
    agree = get_object_or_404(Agreeement, pk=id_agreement)
    doctos = Document.objects.filter(agreement=id_agreement)
    #try:
    now = datetime.today()
    return render_to_response('agreements_detail.html',{'agree':agree, 'doctos':doctos, 'now':now}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
#@permission_required('institution.add_institution')
@permission_required('agreement.add_agreement')
def upload_agreement(request):
    if request.method=='POST':
        formulario = AgreementsForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = AgreementsForm()
    return render_to_response('agreement_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('agreement.change_agreement')
def update_agreement(request, id_agreement):
    obj = get_object_or_404(Agreeement, id=id_agreement)
    formulario = AgreementsUpdate(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_agreement)
    return render_to_response('agreement_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def list_agreement(request):
    site1 = Site.objects.get(id=1).domain
    agree = Agreeement.objects.all()
    return render_to_response('agreement_list.html',{'items':agree, 'site':site1}, context_instance=RequestContext(request))

@permission_required('agreement.remove_agreement')
@login_required(login_url='/manager/ingresar')
def remove_agreement(request, id_agreement, template='agreement_remove.html'):
    try:
        agree = get_object_or_404(Agreeement, id=id_agreement)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "agree": agree
            }))
        if request.method == 'POST':
            agree.delete()
            return HttpResponseRedirect(reverse("list_agreement"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this list_agreement',
            mimetype="text/plain",
            status=401
        )

@login_required(login_url='/manager/ingresar')
def search_agreement(request):
    if request.is_ajax():
        query = request.GET['nombre']
        vigente = request.GET['vigente']
        todos = request.GET['todos']
        now = date.today()
        if query:
            request = getAll(query)#Agreeement.objects.filter(qset).distinct().values('prog_number', 'id', 'legasl_instrument','modal','version_docto')

        else:
            request = []
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
def search_valid(request):
    if request.is_ajax():
        vigente = request.GET['vigente']
        todos = request.GET['todos']
        if vigente:
            request = getValid()
        elif todos:
            request = getInValid()
        else:
            request = []
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
def search_all(request):
    if request.is_ajax():
        request = getAll()
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
def detail_agreement_ajax(request):
    if request.is_ajax():
        obj = request.GET['nombre']
        agree = get_object_or_404(Agreeement, pk=obj)
        return HttpResponseRedirect('../../')
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
def export_agreement(request):
    response =  WriteToExcel(True)

    return response
