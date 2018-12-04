# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0004_auto_20180112_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendFmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dimension', models.CharField(help_text='Dimensi\xf3n ligada', max_length=250, null=True, verbose_name='Dimensi\xf3n', blank=True)),
                ('objetive', models.CharField(help_text='Objetivo ligado', max_length=250, null=True, verbose_name='Objetivo', blank=True)),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('topic', models.ForeignKey(verbose_name='Tema', blank=True, to='forum.Topic', null=True)),
                ('user_follow', models.ForeignKey(related_name='us_follow', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_owner', models.ForeignKey(related_name='us_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TokenF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.TextField(max_length=1000, verbose_name='subject')),
                ('body', models.TextField(max_length=1000, verbose_name='body')),
                ('token', models.TextField(max_length=100, verbose_name='Token')),
                ('comment_html', models.TextField(verbose_name='mail html')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
                ('is_autorized', models.BooleanField(default=False)),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True)),
                ('send', models.ForeignKey(verbose_name='Tema', blank=True, to='fmail.SendFmail', null=True)),
                ('user', models.ForeignKey(related_name='us_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
