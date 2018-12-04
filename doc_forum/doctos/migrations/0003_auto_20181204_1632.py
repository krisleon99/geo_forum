# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import doc_forum.doctos.validators
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('doctos', '0002_auto_20171213_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='author',
            field=models.CharField(help_text=b'Autor del documento', max_length=250, verbose_name=b'*Autor'),
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.TextField(max_length=250, null=True, verbose_name=b'Comentarios', blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='dimension',
            field=models.CharField(max_length=250, verbose_name=b'*Dimensi\xc3\xb3n', choices=[(b'1', b'GENERAL'), (b'2', b'CONTEXTO TERRITORIAL'), (b'3', b'DIMENSI\xc3\x93N GEOPOL\xc3\x8dTICA'), (b'4', b'DIMENSI\xc3\x93N DE SEGURIDAD'), (b'5', b'DIMENSI\xc3\x93N DE INSTITUCIONAL'), (b'6', b'DIMENSI\xc3\x93N LABORAL Y ECON\xc3\x93MICA'), (b'7', b'DIMENSI\xc3\x93N SOCIAL Y CULTURAL'), (b'8', b'DIMENSI\xc3\x93N ASENTAMIENTOS HUMANOS, CIUDADES Y MARCO AMBIENTAL')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='docto_pro',
            field=models.FileField(validators=[doc_forum.doctos.validators.validate_file_extension], upload_to=b'documents/%Y/%m/%d', blank=True, help_text=b'Selecciona un documento o ingresa una URL, donde se encuentre el documento', null=True, verbose_name=b'Selecciona el documento'),
        ),
        migrations.AlterField(
            model_name='document',
            name='objetive',
            field=models.CharField(max_length=2, verbose_name=b'*Objetivo', choices=[(b'a', b'a'), (b'b', b'b'), (b'c', b'c'), (b'd', b'd'), (b'e', b'e'), (b'f', b'f'), (b'g', b'g'), (b'h', b'h'), (b'i', b'i'), (b'j', b'j'), (b'k', b'k'), (b'l', b'l'), (b'm', b'm'), (b'n', b'n'), (b'o', b'o'), (b'p', b'p'), (b'q', b'q'), (b'r', b'r'), (b's', b's'), (b't', b't'), (b'u', b'u'), (b'v', b'v'), (b'w', b'w'), (b'x', b'x'), (b'y', b'y'), (b'z', b'z'), (b'aa', b'aa'), (b'bb', b'bb'), (b'cc', b'cc'), (b'dd', b'dd'), (b'ee', b'ee'), (b'ff', b'ff'), (b'gg', b'gg'), (b'hh', b'hh'), (b'ii', b'ii'), (b'jj', b'jj'), (b'zz', b'zz')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(help_text=b'T\xc3\xadtulo del documento', max_length=250, verbose_name=b'*T\xc3\xadtulo'),
        ),
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.CharField(validators=[django.core.validators.URLValidator()], max_length=100, blank=True, help_text=b'Documento externo', null=True, verbose_name=b'URL'),
        ),
        migrations.AlterField(
            model_name='document',
            name='user',
            field=models.ForeignKey(related_name='us_docto', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Usuario que sube el documento', null=True, verbose_name=b'Usuario'),
        ),
    ]
