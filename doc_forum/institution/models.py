#encoding:utf-8
import logging
from django.db import models

# IMGTYPES = ['jpg', 'jpeg', 'tif', 'tiff', 'png', 'gif']
logger = logging.getLogger(__name__)

class Institution(models.Model):
    name = models.CharField(verbose_name = "Nombre", max_length=250)
    alias = models.CharField(verbose_name = "Siglas", max_length=250)
    legal_representative = models.CharField(verbose_name = "Representante legal", max_length=250,null=True, blank=True)
    #type = models.CharField(verbose_name = "Tipo", max_length=25)
    creation_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
