# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import doc_forum.doctos.validators
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name=b'*Titulo')),
                ('dimension', models.CharField(blank=True, max_length=250, null=True, verbose_name=b'Dimensi\xc3\xb3n', choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd'), (b'e', b'e'), (b'f', b'f'), (b'g', b'g'), (b'h', b'h')])),
                ('objetive', models.CharField(blank=True, max_length=2, null=True, verbose_name=b'Objetivo', choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8')])),
                ('docto_pro', models.FileField(blank=True, upload_to=b'documents/%Y/%m/%d', null=True, verbose_name=b'Selecciona el documento', validators=[doc_forum.doctos.validators.validate_file_extension])),
                ('url', models.CharField(blank=True, max_length=100, null=True, help_text=b'o Documento externo', validators=[django.core.validators.URLValidator()])),
                ('author', models.CharField(max_length=250, verbose_name=b'Autor')),
                ('description', models.TextField(max_length=250, verbose_name=b'Descripcion del Convenio')),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
