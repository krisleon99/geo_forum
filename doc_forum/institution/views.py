from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Institution
from .forms import Institution_Form, Institution_Update

@login_required(login_url='/manager/ingresar')
def list_institution(request):
    agree = Institution.objects.all()
    return render_to_response('institution_list.html',{'items':agree}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('institution.add_institution')
def upload_institution(request):
    if request.method=='POST':
        formulario = Institution_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Institution_Form()
    return render_to_response('institution_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('institution.change_institution')
def update_institution(request, id_institution):
    obj = get_object_or_404(Institution, id=id_institution)
    formulario = Institution_Update(request.POST or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    return render_to_response('institution_form.html',{'formulario':formulario}, context_instance=RequestContext(request))
