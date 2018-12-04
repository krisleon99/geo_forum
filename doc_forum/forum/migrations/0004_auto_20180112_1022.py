# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20171204_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='comment',
            field=models.TextField(max_length=1000, verbose_name='T\xedtulo (Largo)'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=255, verbose_name='T\xedtulo (Corto)'),
        ),
    ]
