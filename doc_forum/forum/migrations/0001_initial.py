# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(max_length=1000, verbose_name='Comentario')),
                ('image', models.ImageField(help_text='Adjuntar foto', upload_to='images/chats-map/', null=True, verbose_name='Imagen', blank=True)),
                ('comment_html', models.TextField(verbose_name='comment html')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_removed', models.BooleanField(default=False)),
                ('is_modified', models.BooleanField(default=False)),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True)),
                ('modified_count', models.PositiveIntegerField(default=0, verbose_name='modified count')),
                ('likes_count', models.PositiveIntegerField(default=0, verbose_name='likes count')),
            ],
        ),
        migrations.CreateModel(
            name='ForumLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_like', models.BooleanField(verbose_name='like')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('forum', models.ForeignKey(related_name='forum_likes', verbose_name='like', blank=True, to='forum.Forum', null=True)),
                ('user', models.ForeignKey(related_name='st_comment_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyForum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(max_length=1000, verbose_name='Comentario')),
                ('image', models.ImageField(help_text='Im\xe1gen', upload_to='images/chats-map/', null=True, verbose_name='Imagen', blank=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.URLValidator()])),
                ('status', models.BooleanField(verbose_name='Estaus')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(related_name='forum_reply', verbose_name='Forum', blank=True, to='forum.Forum', null=True)),
                ('user_reply', models.ForeignKey(related_name='user_forum_reply', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('comment', models.TextField(max_length=1000, verbose_name='description_tp')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('last_active', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last active')),
                ('is_pinned', models.BooleanField(default=False, verbose_name='pinned')),
                ('is_globally_pinned', models.BooleanField(default=False, verbose_name='globally pinned')),
                ('is_closed', models.BooleanField(default=False, verbose_name='closed')),
                ('is_removed', models.BooleanField(default=False)),
                ('view_count', models.PositiveIntegerField(default=0, verbose_name='views count')),
                ('comment_count', models.PositiveIntegerField(default=0, verbose_name='comment count')),
                ('user', models.ForeignKey(related_name='us_topics', to=settings.AUTH_USER_MODEL)),
                ('users_private', models.ManyToManyField(related_name='users_private', verbose_name='Usuarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='forum',
            name='topic',
            field=models.ForeignKey(verbose_name='Tema', blank=True, to='forum.Topic', null=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='user',
            field=models.ForeignKey(related_name='us_forum', to=settings.AUTH_USER_MODEL),
        ),
    ]
