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

from .models import Agreementgs, Conacyt_fund, PeopleContac, Accomplishment
from .forms import AgreementsForm, AgreementsEspForm, Conacyt_fundForm, PeopleContacForm, AccomplishmentForm, AgreementsProgressForm, AgreementsUpdate, AgreementsEspUpdate, Conacyt_fundUpdate, PeopleContacUpdate, AccomplishmentUpdate, Add_Accomplishment, AgreementsEspResourcese
from doc_forum.doctos.models import Document
from doc_forum.doctos.forms import Docto_Update
from django.contrib.sites.models import Site

# Create your views here.
@login_required(login_url='/manager/ingresar')
def list_agreementgesp(request):
    agree = Document.objects.all()
    return render_to_response('agreementgs_list.html',{'items':agree, 'SITE_URL': Site.objects.get_current()}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.add_agreementgs')
def upload_agreementgesp(request):
    if request.method=='POST':
        formulario = AgreementsForm(request.POST, request.FILES)
        if formulario.is_valid():
            form = formulario.save()
            return HttpResponseRedirect('../'+str(form.pk))
    else:
        formulario = AgreementsForm()
    return render_to_response('agreementgs_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.add_agreementgs')
def upload_agreementgesp_esp(request):
    if request.method=='POST':
        formulario = AgreementsEspForm(request.POST, request.FILES)
        if formulario.is_valid():
            esp_form = formulario.save()
            esp_form.agreement_type = 'Especifico'
            esp_form.save()
            return HttpResponseRedirect('../'+str(esp_form.pk))
    else:
        formulario = AgreementsEspForm()
    return render_to_response('agreementgs_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def detail_agreementgesp(request, id_agreement):
    formato = "%d/%m/%Y"
    agree = get_object_or_404(Document, pk=id_agreement)
    count = agree.description.count('#')
    now = datetime.today()
    return render_to_response('agreementgs_detail.html',{'agree':agree, 'count':count}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def update_agreementgesp(request, id_agreement):
    obj = get_object_or_404(Agreementgs, id=id_agreement)
    formulario = AgreementsUpdate(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_agreement)
    return render_to_response('agreementgs_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def update_agreementgesp_esp(request, id_agreement):
    def get_initial(self):
        return {'agreement_type' : 'Especifico'}
    obj = get_object_or_404(Document, id=id_agreement)
    formulario = Docto_Update(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_agreement)
    return render_to_response('agreementgs_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def list_conacyt_fund(request):
    conacyt_fund = Conacyt_fund.objects.all()
    return render_to_response('conacyt_fund_list.html',{'items':conacyt_fund}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.add_agreementgs')
def upload_conacyt_fund(request):
    if request.method=='POST':
        formulario = Conacyt_fundForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Conacyt_fundForm()
    return render_to_response('conacyt_fund_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def update_conacyt_fund(request, id_cf):
    obj = get_object_or_404(Conacyt_fund, id=id_cf)
    formulario = Conacyt_fundUpdate(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_cf)
    return render_to_response('conacyt_fund_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def list_accomplishment(request):
    accomplishment = Accomplishment.objects.all()
    return render_to_response('accomplishment_list.html',{'items':accomplishment}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreement.add_agreement')
def upload_accomplishment(request):
    if request.method=='POST':
        formulario = AccomplishmentForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = AccomplishmentForm()
    return render_to_response('accomplishment_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def update_accomplishment(request, id_accom):
    obj = get_object_or_404(Accomplishment, id=id_accom)
    formulario = AccomplishmentUpdate(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_accom)
    return render_to_response('accomplishment_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def upload_accomplishment_agreement(request, id_agreement):
    if request.method=='POST':
        agre = get_object_or_404(Agreementgs, pk=id_agreement)
        formulario = AccomplishmentUpdate(request.POST, request.FILES)
        if formulario.is_valid():
            instance = Accomplishment(description=request.POST.get("description", ""),agreementgs=agre)
            instance.save()
            return HttpResponseRedirect('../../agreementgesp/'+id_agreement)
    else:
        formulario = Add_Accomplishment()
    return render_to_response('add_accomplishment.html',{'formulario':formulario,'id_proposal':id_agreement}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def list_peoplecontac(request):
    peoplecontac = PeopleContac.objects.all()
    return render_to_response('peoplecontac_list.html',{'items':peoplecontac}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.add_agreementgs')
def upload_peoplecontac(request):
    if request.method=='POST':
        formulario = PeopleContacForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = PeopleContacForm()
    return render_to_response('peoplecontac_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def update_peoplecontac(request, id_peop):
    obj = get_object_or_404(PeopleContac, id=id_peop)
    formulario = PeopleContacUpdate(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_peop)
    return render_to_response('peoplecontac_form.html',{'formulario':formulario}, context_instance=RequestContext(request))


def save_progress(request):
    if request.is_ajax():
        data_list = []
        query_data = json.loads(request.POST['query_data'])
        id_ms=query_data['id_ms']
        id_color = query_data['id_color']
        try:
            obj = get_object_or_404(Agreementgs, id=id_ms)
            colors_form = AgreementsProgressForm({'progress': id_color}, instance = obj)
            if colors_form.is_valid():
                colors_form.save()
            return HttpResponse( json.dumps(data_list), content_type='application/json' )
        except Agreementgs.DoesNotExist:
            print("Error No existe el objeto")
            return HttpResponse( json.dumps(data_list), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.delete_agreementgs')
def remove_agreementgesp(request, id_agreement, template='agreementgs_remove.html'):
    try:
        agree = get_object_or_404(Agreementgs, id=id_agreement)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "agree": agree
            }))
        if request.method == 'POST':
            agree.delete()
            return HttpResponseRedirect(reverse("list_agreementgesp"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this list_agreement',
            mimetype="text/plain",
            status=401
        )


@login_required(login_url='/manager/ingresar')
@permission_required('agreementgesp.change_agreementgs')
def resourcese_agreementgesp(request, id_agreement):
    obj = get_object_or_404(Agreementgs, id=id_agreement)
    formulario = AgreementsEspResourcese(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_agreement)
    return render_to_response('agreementgs_form.html',{'formulario':formulario}, context_instance=RequestContext(request))
