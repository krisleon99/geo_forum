# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Nombre')),
                ('description', models.TextField(max_length=250, null=True, verbose_name=b'Descripcion', blank=True)),
                ('dimension', models.CharField(blank=True, max_length=250, null=True, verbose_name=b'Dimensi\xc3\xb3n', choices=[(b'1', b'GENERAL')])),
                ('objetive', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'Objetivo', choices=[(b'a', b'a')])),
                ('start_date', models.DateField(null=True, verbose_name=b'Fecha de inicio', blank=True)),
                ('end_date', models.DateField(null=True, verbose_name=b'Fecha de Fin', blank=True)),
                ('start_hour', models.TimeField(null=True, verbose_name=b'Fecha de inicio', blank=True)),
                ('end_hour', models.TimeField(null=True, verbose_name=b'Fecha fin', blank=True)),
                ('is_public', models.BooleanField(default=False, verbose_name=b'P\xc3\xbablico')),
                ('is_finally', models.BooleanField(default=False, verbose_name=b'Finalizado')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('participants', models.ManyToManyField(related_name='participants_event', null=True, verbose_name=b'Participantes', to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(related_name='us_event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
