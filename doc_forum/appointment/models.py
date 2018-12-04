#encoding:utf-8
import logging
from django.db import models
from django.conf import settings

# IMGTYPES = ['jpg', 'jpeg', 'tif', 'tiff', 'png', 'gif']
logger = logging.getLogger(__name__)

class Event(models.Model):
    DIMENSIONS = (
        ('1', 'GENERAL'),
        )
    OBJETIVES = (
        ('a', 'a'),
        )
    name = models.CharField(verbose_name = "Nombre", max_length=250)
    description = models.TextField(verbose_name='Descripcion', max_length=250, null=True, blank=True)
    dimension = models.CharField(verbose_name = "Dimensión", max_length=250, choices=DIMENSIONS, blank=True, null=True)
    objetive = models.CharField(max_length=2, choices=OBJETIVES, verbose_name = "Objetivo", blank=True, null=True)
    start_date = models.DateField(verbose_name='Fecha de inicio', null=True, blank=True)
    end_date = models.DateField(verbose_name='Fecha de Fin', null=True, blank=True)
    start_hour = models.TimeField(verbose_name='Fecha de inicio', null=True, blank=True)
    end_hour = models.TimeField(verbose_name='Fecha fin', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_event')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants_event', verbose_name = "Participantes", null=True, blank=True)
    is_public = models.BooleanField(verbose_name = "Público", default=False)
    is_finally = models.BooleanField(verbose_name = "Finalizado", default=False)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
