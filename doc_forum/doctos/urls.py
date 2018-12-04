# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.doctos',),
}

urlpatterns = [

               url(r'^upload_document/$', views.upload_document, name='upload_document'),

               url(r'^upload_pro/(?P<id_proposal>\d+)/?$', views.upload_docto_proposal, name='upload_docto_proposal'),

               url(r'^upload_agre/(?P<id_agreement>\d+)/?$', views.upload_docto_agreement, name='upload_docto_agreement'),

               url(r'^delete/(?P<id_docto>\d+)/?$', views.delete_docto, name='delete_docto'),

               ]
