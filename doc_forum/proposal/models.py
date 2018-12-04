#encoding:utf-8
import logging
from django.db import models
from datetime import datetime
from django.db.models import Q
from django.conf import settings

IMGTYPES = ['jpg', 'jpeg', 'tif', 'tiff', 'png', 'gif']

logger = logging.getLogger(__name__)

class Proposal(models.Model):
    call_background = models.CharField(verbose_name = "*Fondo/Convocatoria", max_length=250)
    project = models.IntegerField(verbose_name = "Proyecto",null=True, blank=True, unique=True)
    title = models.CharField(verbose_name = "*Titulo", max_length=250)
    techical_responsible = models.CharField(verbose_name = "Responsable Técnico", max_length=250,null=True, blank=True)
    request_amount = models.DecimalField(verbose_name = "Monto Solicitado", max_digits=9, decimal_places=3,null=True, blank=True)
    authorized_amount = models.DecimalField(verbose_name = "Monto Autorizado", max_digits=9, decimal_places=3,null=True, blank=True)
    transfer = models.DecimalField(verbose_name = "Transferencia", max_digits=9, decimal_places=3,null=True, blank=True)
    observation = models.TextField(verbose_name='*Observaciones', max_length=250)
    validity_date = models.DateTimeField(verbose_name = "Vigencia",default=datetime.now,help_text="Fecha Final de la propuesta",null=True, blank=True)
    proposal_name = models.CharField(verbose_name = "Propuesta", max_length=250, null=True, blank=True)
    docfile_proposal = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona un documento para la propuesta ",null=True, blank=True)
    docto_name_pro_acept = models.CharField(verbose_name = "Documento Aceptado", max_length=250, null=True, blank=True)
    docto_pro_acept = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento Aceptado",null=True, blank=True)
    docto_legal_pro_name = models.CharField(verbose_name = "Documento Legal", max_length=250, null=True, blank=True)
    docto_legal_pro = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento Legal",null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

def getValid():
    print "vigente-_-"
    now = datetime.today()
    print now
    agre = Proposal.objects.filter(validity_date__gt=datetime.date(now)).values('title', 'id', 'project','call_background','techical_responsible','observation','proposal_name')
    print agre
    return agre

def getInValid():
    print "not vigente-_-"
    now = datetime.today()
    print now
    agre = Proposal.objects.exclude(validity_date__gt=datetime.date(now)).values('title', 'id', 'project','call_background','techical_responsible','observation','proposal_name')
    print agre
    return agre

def getAllFilter(query):
    print "query all"
    qset = (
            Q(call_background__contains=query) |
            Q(title__contains=query) |
            Q(techical_responsible__contains=query) |
            Q(observation__contains=query)
            )
    print qset
    request = Proposal.objects.filter(qset).distinct().values('title', 'id', 'project','call_background','techical_responsible','observation','proposal_name')
    return request

def getAll():
    request = Proposal.objects.all().distinct().values('title', 'id', 'project','call_background','techical_responsible','observation','proposal_name')
    return request