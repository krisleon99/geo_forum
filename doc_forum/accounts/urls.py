# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.accounts',),
}

urlpatterns = [

               url(r'^login/$', views.denied_access, name='denied_access'),

               ]
