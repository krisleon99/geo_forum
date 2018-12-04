#encoding:utf-8
import logging
from django.db import models
from datetime import datetime
from django.db.models import Q

from doc_forum.institution.models import Institution


logger = logging.getLogger(__name__)

class Conacyt_fund(models.Model):
	parent_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name = "Fondo", related_name='children', null=True, blank=True)
	title = models.CharField(verbose_name = "Título", max_length=250, null=False, blank=False)

	def __unicode__(self):
		return self.title

class PeopleContac(models.Model):
	name = models.CharField(verbose_name = "Nombre Completo", max_length=250, null=False, blank=False)

	def __unicode__(self):
		return self.name

class Agreementgs(models.Model):
	setid = models.CharField(verbose_name = "ID", max_length=250, null=False, blank=False)
	UNITY_NAME_CHOICES = (('CDMX', 'CDMX'),('AGS', 'AGS'),('YUC', 'YUC'))
	unity_name = models.CharField(verbose_name = "Nombre de la unidad", max_length=100, choices=UNITY_NAME_CHOICES, default='CDMX')
	AMBIT = (('Nacional', 'Nacional'),('Internacional', 'Internacional'))
	ambit = models.CharField(verbose_name = "Ámbito", max_length=100, choices=AMBIT, default='Nacional')
	AG_TYPE = (('General','General'),('Especifico','Específico'))
	agreement_type = models.CharField(verbose_name = "Tipo de convenio",  max_length=100, choices=AG_TYPE, default='General')
	PRO_TYPE = (('Interinstitucional','Interinstitucional'),('Investigacion','Investigación'))
	project_type = models.CharField(verbose_name = "Modalidad del proyecto", max_length=100, choices=PRO_TYPE)
	project_name = models.CharField(verbose_name = "Nombre del proyecto", max_length=250, null=True)
	project_key = models.CharField(verbose_name = "Clave del proyecto", max_length=250)
	objective = models.TextField(verbose_name = "Objetivo del convenio", max_length=500)
	conacyt_fund = models.ManyToManyField(Conacyt_fund, verbose_name='Fondo CONACYT', blank=True)
	other_financing = models.ManyToManyField(Institution, related_name="Otra_institucion", verbose_name="Otras agencias de financiamiento", blank=True)
	institution = models.ManyToManyField(Institution, related_name='Institucion', verbose_name="Institución vinculada", blank=True)
	PRO_TYPE_2 = (('Investigacion','Investigación'),('Desarrollo tecnologico','Desarrollo tecnológico'),('Servicio','Servicio'))
	project_type_2 = models.CharField(verbose_name = "Tipo de proyecto", max_length=100, choices=PRO_TYPE_2)
	start_date = models.DateField(verbose_name='Fecha de inicio')
	end_date = models.DateField(verbose_name='Fecha de termino')
	technical_support = models.ManyToManyField(PeopleContac, verbose_name = "Responsable técnico", blank=True)
	RESOURCES = (('Si','Sí'),('No','No'))
	resources = models.CharField(verbose_name = "Tiene recursos", max_length=100, choices=RESOURCES, default='No')
	authorized_amount = models.IntegerField(verbose_name = "Monto autorizado", null=True)
	authorized_implemented = models.IntegerField(verbose_name = "Monto ejecutado", null=True)
	PROJECT_C = (('Si','Sí'),('No','No'))
	project_completed = models.CharField(verbose_name = "Proyecto concluido", max_length=100, choices=PROJECT_C, default='No')
	progress = models.IntegerField(verbose_name = "Avance", default=0)
	comments = models.TextField(verbose_name='Comentarios', max_length=500, null=True, blank=True)
	#document = models.ManyToManyField(Document, verbose_name = "Documents", blank=True)
	creation_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.setid

class Accomplishment(models.Model):
	agreementgs = models.ForeignKey(Agreementgs, verbose_name = "Convenio",null=True, blank=True)
	description = models.CharField(verbose_name = "Logro", max_length=250, null=False, blank=False)

	def __unicode__(self):
		return self.description
