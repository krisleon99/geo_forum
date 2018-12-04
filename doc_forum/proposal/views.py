from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, permission_required
import json
from django.contrib.sites.models import Site
from datetime import date

from doc_forum.doctos.models import Document
from doc_forum.manager.excel_utils import WriteToExcel
from .models import Proposal, getAll, getInValid, getValid, getAllFilter
from .forms import ProposalForm, ProposalUpdate

@login_required(login_url='/manager/ingresar')
def list_proposal(request):
    pro = Proposal.objects.all()
    site1 = Site.objects.get(id=1).domain
    return render_to_response('proposal_list.html',{'items':pro,'site':site1}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('proposal.add_proposal')
def upload_proposal(request):
    if request.method=='POST':
        formulario = ProposalForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = ProposalForm()
    return render_to_response('proposal_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def detail_proposal(request, id_proposal):
    pro = get_object_or_404(Proposal, pk=id_proposal)
    doctos = Document.objects.filter(proposal=id_proposal)
    residue = pro.authorized_amount-pro.transfer
    now = date.today()
    print now
    return render_to_response('proposal_detail.html',{'prop':pro,'doctos':doctos, 'saldo_ejercido':residue, 'now':now}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
@permission_required('proposal.change_proposal')
def update_proposal(request, id_proposal):
    obj = get_object_or_404(Proposal, id=id_proposal)
    formulario = ProposalUpdate(request.POST or None,request.FILES or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../'+ id_proposal)
    return render_to_response('proposal_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('proposal.remove_proposal')
def remove_proposal(request, id_proposal, template='proposal_remove.html'):
    try:
        pro = get_object_or_404(Proposal, id=id_proposal)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "agree": pro
            }))
        if request.method == 'POST':
            pro.delete()
            return HttpResponseRedirect(reverse("list_proposal"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this list_proposal',
            mimetype="text/plain",
            status=401
        )

def search_proposal(request):
    if request.is_ajax():
        query = request.GET['nombre']
        if query:
            print query
            request = getAllFilter(query)
        else:
            request = []
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

def search_valid(request):
    if request.is_ajax():
        vigente = request.GET['vigente']
        todos = request.GET['todos']
        if vigente:
            request = getValid()
            print "vigente yupi"
            print request
            print "finish"
        elif todos:
            request = getInValid()
            print "no es vigente"
            print request
        else:
            request = []
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

def search_all(request):
    if request.is_ajax():
        request = getAll()
        return HttpResponse( json.dumps( list(request)), content_type='application/json' )
    else:
        return HttpResponse("Solo Ajax")

@login_required(login_url='/manager/ingresar')
def export_proposal(request):
    response =  WriteToExcel(False)

    return response
