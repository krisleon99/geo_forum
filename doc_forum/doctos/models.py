#encoding:utf-8
import logging
from .validators import validate_file_extension
from django.core.validators import URLValidator
from django.db import models
from django.conf import settings

IMGTYPES = ['jpg', 'jpeg', 'tif', 'tiff', 'png', 'gif']

logger = logging.getLogger(__name__)

class Document(models.Model):
	DIMENSIONS = (
		('1', 'GENERAL'),
		('2', 'CONTEXTO TERRITORIAL'),
		('3', 'DIMENSIÓN GEOPOLÍTICA'),
		('4', 'DIMENSIÓN DE SEGURIDAD'),
		('5', 'DIMENSIÓN DE INSTITUCIONAL'),
		('6', 'DIMENSIÓN LABORAL Y ECONÓMICA'),
		('7', 'DIMENSIÓN SOCIAL Y CULTURAL'),
		('8', 'DIMENSIÓN ASENTAMIENTOS HUMANOS, CIUDADES Y MARCO AMBIENTAL'),
		)
	OBJETIVES = (
		('a', 'a'),
		('b', 'b'),
		('c', 'c'),
		('d', 'd'),
		('e', 'e'),
		('f', 'f'),
		('g', 'g'),
		('h', 'h'),
		('i', 'i'),
		('j', 'j'),
		('k', 'k'),
		('l', 'l'),
		('m', 'm'),
		('n', 'n'),
		('o', 'o'),
		('p', 'p'),
		('q', 'q'),
		('r', 'r'),
		('s', 's'),
		('t', 't'),
		('u', 'u'),
		('v', 'v'),
		('w', 'w'),
		('x', 'x'),
		('y', 'y'),
		('z', 'z'),
		('aa', 'aa'),
		('bb', 'bb'),
		('cc', 'cc'),
		('dd', 'dd'),
		('ee', 'ee'),
		('ff', 'ff'),
		('gg', 'gg'),
		('hh', 'hh'),
		('ii', 'ii'),
		('jj', 'jj'),
		('zz', 'zz'),
		)
	title = models.CharField(verbose_name = "*Título", max_length=250, help_text="Título del documento")
	dimension = models.CharField(verbose_name = "*Dimensión", max_length=250, choices=DIMENSIONS, blank=False, null=False)
	objetive = models.CharField(max_length=2, choices=OBJETIVES, verbose_name = "*Objetivo", blank=False, null=False)
	docto_pro = models.FileField(upload_to='documents/%Y/%m/%d', verbose_name = "Selecciona el documento",  help_text="Selecciona un documento o ingresa una URL, donde se encuentre el documento", validators=[validate_file_extension], blank=True, null=True)
	url = models.CharField(validators=[URLValidator()], verbose_name="URL",max_length=100, null=True, blank=True, help_text='Documento externo')
	author = models.CharField(verbose_name = "*Autor", help_text="Autor del documento" ,max_length=250, null=False, blank=False)
	description = models.TextField(verbose_name='Comentarios', max_length=250, null=True, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuario', help_text="Usuario que sube el documento",related_name='us_docto', null=True, blank=True)
	creation_date = models.DateField(auto_now_add=True)
	def __unicode__(self):
		return self.title
