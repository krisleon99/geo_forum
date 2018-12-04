#encoding:utf-8
import logging
from django.db import models
from datetime import datetime
from django.db.models import Q

from doc_forum.institution.models import Institution

IMGTYPES = ['jpg', 'jpeg', 'tif', 'tiff', 'png', 'gif']

logger = logging.getLogger(__name__)

class Agreeement(models.Model):
    prog_number = models.IntegerField(verbose_name = "*Número de Programa", unique=True, null=False, blank=False)
    legasl_instrument = models.CharField(verbose_name = "*Instrumento Legal Subscrito", max_length=250, null=False, blank=False)
    docfile_legasl_instrument = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "*Selecciona un documento para el instrumento legal ", null=False, blank=False)
    document_classification = models.CharField(verbose_name = "Clasificacion del Documento", max_length=250, null=True, blank=True)
    registration_number = models.IntegerField(verbose_name = "Numero de Registro",null=True, blank=True)
    conterpart_institution = models.ForeignKey(Institution, verbose_name = "Institución",null=True, blank=True)
    conterpart_institution_acroniym = models.CharField(verbose_name = "Otra Institucion", max_length=100,null=True, blank=True)
    subscription_field = models.CharField(verbose_name = "Ambito de Subscripcion", max_length=250,null=True, blank=True)
    conterpart_sector = models.CharField(verbose_name = "Sector Contraparte", max_length=250,null=True, blank=True)
    description = models.TextField(verbose_name='*Descripcion del Convenio', max_length=250)
    signature_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Firma', help_text="fecha de firma",null=True, blank=True)
    # start_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Inicio',help_text="fecha de inicio")
    end_date = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Termino', help_text="fecha de termino",null=True, blank=True)
    # duration = models.CharField(verbose_name = "Duracion", max_length=250)
    # status = models.BooleanField(verbose_name = "Vigente", default=False)
    modal = models.CharField(verbose_name = "Modalidad del Instrumento", max_length=250, null=True, blank=True)
    version_docto = models.CharField(verbose_name = "Version del documento", max_length=150, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    docto_name_acept = models.CharField(verbose_name = "Documento Aceptado", max_length=250, null=True, blank=True)
    docto_acept = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento Aceptado",null=True, blank=True)
    docto_legal_name = models.CharField(verbose_name = "Documento Legal", max_length=250, null=True, blank=True)
    docto_legal = models.FileField(upload_to='documents/', verbose_name = "Selecciona el documento Legal",null=True, blank=True)

    def __unicode__(self):
        return self.legasl_instrument

def getValid():
    print "vigente-_-"
    now = datetime.today()
    print now
    agre = Agreeement.objects.filter(end_date__gt=datetime.date(now)).values('prog_number', 'id', 'legasl_instrument','modal','version_docto')
    print agre
    return agre

def getInValid():
    print "not vigente-_-"
    now = datetime.today()
    print now
    agre = Agreeement.objects.exclude(end_date__gt=datetime.date(now)).values('prog_number', 'id', 'legasl_instrument','modal','version_docto')
    print agre
    return agre

def getAll(query):
     qset = (
            Q(legasl_instrument__contains=query) |
            Q(version_docto__contains=query) |
            Q(modal__contains=query)
            )
     print qset
     request = Agreeement.objects.filter(qset).distinct().values('prog_number', 'id', 'legasl_instrument','modal','version_docto')
     return request

def getAll():
     request = Agreeement.objects.all().distinct().values('prog_number', 'id', 'legasl_instrument','modal','version_docto')
     return request
