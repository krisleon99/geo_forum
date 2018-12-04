# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import URLValidator
from django.utils import timezone
from doc_forum.forum.models import Topic

from django.conf import settings


class SendFmail(models.Model):
    """
    Send Email Forum model
    :send a emalil for join users whit others users\
    send a emalil for join users whit dimensios, objetives or forums,\
    """
    user_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_owner')
    user_follow = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_follow', null=True, blank=True)
    dimension = models.CharField(verbose_name = "Dimensión", max_length=250, help_text="Dimensión ligada", null=True, blank=True)
    objetive = models.CharField(verbose_name = "Objetivo", max_length=250, help_text="Objetivo ligado", null=True, blank=True)
    topic = models.ForeignKey(Topic, verbose_name = "Tema", null=True, blank=True)
    status = models.BooleanField(verbose_name = "Estatus", default=True)
    creation_date = models.DateTimeField(_("date"), default=timezone.now)

    def __unicode__(self):
        return self.user_owner.username


class TokenF(models.Model):
    """
    Thar Tokenm is like history for send email for forum
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_token')
    send = models.ForeignKey(SendFmail, verbose_name = "Tema", null=True, blank=True)
    subject = models.TextField(verbose_name='subject', max_length=1000)
    body = models.TextField(verbose_name='body', max_length=1000)
    token = models.TextField(verbose_name='Token', max_length=100)
    comment_html = models.TextField(_("mail html"))
    creation_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    is_autorized = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __unicode__(self):
        return self.token
