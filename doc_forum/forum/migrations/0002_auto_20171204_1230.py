# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='comment',
            field=models.TextField(max_length=1000, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_active',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='last active', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='users_private',
            field=models.ManyToManyField(related_name='users_private', null=True, verbose_name='Usuarios', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
