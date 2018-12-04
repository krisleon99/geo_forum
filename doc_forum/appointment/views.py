import dateutil.parser
import logging
import json

from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render
from django.utils import timezone
from datetime import date

from .models import Event
from doc_forum.appointment.forms import Event_Form, Event_Update

# Get an instance of a logger
logger = logging.getLogger(__name__)
dbalogger = logging.getLogger('appointment')

@login_required(login_url='/manager/ingresar')
def event_detail(request, id_event):
    event = get_object_or_404(Event, id=id_event)
    return render_to_response('event_detail.html',{'event':event}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
# @permission_required('agreement.change_agreement')
def update_event(request, id_event):
    obj = get_object_or_404(Event, id=id_event)
    formulario = Event_Update(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse("agreement_and_proposal"))
    return render_to_response('event_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

def event_save(request):
    if request.is_ajax():
        try:
            data_list = []
            id_user_loged = request.user.id
            query_data = json.loads(request.POST['query_data'])
            event = query_data['event']
            date_s = query_data['start']
            if event:
                now = timezone.now()
                logger.error('Something went wrong!')
                dt = dateutil.parser.parse(date_s)
                event_form = Event_Form({'name':event,'start_date':dt,'user': id_user_loged, 'creation_date':now})
                print event_form
                if event_form.is_valid():
                    obj = event_form.save()
                    print "sabrinas"
                    print obj
                    day = obj.start_date.strftime('%d')
                    month = obj.start_date.strftime('%m')
                    print day
                    print month
                    data_list.append(obj.id)
                    data_list.append(obj.name)
                    data_list.append(day)
                    data_list.append(month)
                    print data_list

        except ObjectDoesNotExist:
        	print("Error No existe el objeto")
        	return HttpResponse('Event Do not Saved')
        return HttpResponse( json.dumps(data_list), content_type='application/json' )
    else:
        return HttpResponse("Not ajax request")

@login_required(login_url='/manager/ingresar')
# @permission_required('doctos.delete_document')
def delete_event(request, id_event, template='event_remove.html'):
    try:
        ev = get_object_or_404(Event, id=id_event)
        if request.method == 'GET':
            return render_to_response(template, RequestContext(request, {
                "ev": ev
            }))
        if request.method == 'POST':
            ev.delete()
            return HttpResponseRedirect(reverse("agreement_and_proposal"))
        else:
            return HttpResponse("Not allowed", status=403)

    except PermissionDenied:
        return HttpResponse(
            'You are not allowed to delete this agreement_and_proposal',
            mimetype="text/plain",
            status=401
        )
