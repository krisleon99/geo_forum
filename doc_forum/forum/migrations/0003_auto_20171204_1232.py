# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20171204_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='last_active',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last active'),
        ),
    ]
