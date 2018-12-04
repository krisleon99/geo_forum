# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.institution',),
}

urlpatterns = [

               url(r'^$', views.list_institution, name='list_institution'),

               url(r'^upload/$', views.upload_institution, name='upload_institution'),

               url(r'^update/(?P<id_institution>\d+)$', views.update_institution, name='update_institution'),

               ]
