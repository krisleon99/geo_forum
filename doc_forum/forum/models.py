# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import URLValidator
from django.utils import timezone

from django.conf import settings


class Topic(models.Model):
    """
    Topic model

    :ivar last_active: Last time a comment was added/removed,\
    it makes the search re-index the topic
    :vartype last_active: `:py:class:models.DateTimeField`
    :ivar reindex_at: Last time this model was marked\
    for reindex. It makes the search re-index the topic,\
    it must be set explicitly
    :vartype reindex_at: `:py:class:models.DateTimeField`
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_topics')
    # category = models.ForeignKey('spirit_category.Category', verbose_name=_("category"))
    users_private = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_private', verbose_name = "Usuarios", null=True, blank=True)
    title = models.CharField(_("Título (Corto)"), max_length=255)
    comment = models.TextField(verbose_name='Título (Largo)', max_length=1000)
    creation_date = models.DateTimeField(_("date"), default=timezone.now)
    last_active = models.DateTimeField(_("last active"), default=timezone.now)
    is_pinned = models.BooleanField(_("pinned"), default=False)
    is_globally_pinned = models.BooleanField(_("globally pinned"), default=False)
    is_closed = models.BooleanField(_("closed"), default=False)
    is_removed = models.BooleanField(default=False)

    view_count = models.PositiveIntegerField(_("views count"), default=0)
    comment_count = models.PositiveIntegerField(_("comment count"), default=0)

    def __unicode__(self):
        return self.title


class Forum(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='us_forum')
    topic = models.ForeignKey(Topic, verbose_name = "Tema", null=True, blank=True)
    comment = models.TextField(verbose_name='Comentario', max_length=1000)
    image = models.ImageField(verbose_name = "Imagen", help_text='Adjuntar foto', upload_to="images/chats-map/", null=True, blank=True)
    comment_html = models.TextField(_("comment html"))
    creation_date = models.DateTimeField(default=timezone.now)
    is_removed = models.BooleanField(default=False)
    is_modified = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    modified_count = models.PositiveIntegerField(_("modified count"), default=0)
    likes_count = models.PositiveIntegerField(_("likes count"), default=0)

    def __unicode__(self):
        return self.comment

class ForumLike(models.Model):
    is_like = models.BooleanField(verbose_name = "like")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='st_comment_likes')
    forum = models.ForeignKey(Forum, verbose_name = 'like', related_name='forum_likes', null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.forum.comment

class ReplyForum(models.Model):
    forum = models.ForeignKey(Forum, verbose_name = "Forum", related_name='forum_reply', null=True, blank=True)
    user_reply = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = "user_forum_reply", null=True, blank=True)
    comments = models.TextField(verbose_name='Comentario', max_length=1000)
    image = models.ImageField(verbose_name = "Imagen", help_text='Imágen', upload_to="images/chats-map/", null=True, blank=True)
    url = models.CharField(validators=[URLValidator()], max_length=100, null=True, blank=True)
    status = models.BooleanField(verbose_name = "Estaus")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.comments
