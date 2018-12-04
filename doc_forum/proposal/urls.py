# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views

js_info_dict = {
    'packages': ('doc_forum.proposal',),
}

urlpatterns = [
                       url(r'^$', views.list_proposal, name='list_proposal'),

                       url(r'^upload/$', views.upload_proposal, name='upload_proposal'),

                       url(r'^(?P<id_proposal>\d+)/?$', views.detail_proposal, name='detail_proposal'),

                       url(r'^update/(?P<id_proposal>\d+)$', views.update_proposal, name='update_proposal'),

                       url(r'^remove/(?P<id_proposal>\d+)$', views.remove_proposal, name='remove_proposal'),

                       url(r'^searchs/$', views.search_proposal, name='search_proposal'),

                       url(r'^searchvalid/$', views.search_valid, name='search_valid'),

                       url(r'^searchall/$', views.search_all, name='search_all'),

                       url(r'^export$', views.export_proposal, name='export_proposal'),

                       ]
