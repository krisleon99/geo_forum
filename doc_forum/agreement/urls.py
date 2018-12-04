# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.agreement',),
}

urlpatterns = [
                       url(r'^$', views.list_agreement, name='list_agreement'),

                       url(r'^(?P<id_agreement>\d+)/?$', views.detail_agreement, name='detail_agreement'),

                       url(r'^upload/$', views.upload_agreement, name='upload_agreement'),

                       url(r'^update/(?P<id_agreement>\d+)$', views.update_agreement, name='update_agreement'),

                       url(r'^remove/(?P<id_agreement>\d+)$', views.remove_agreement, name='remove_agreement'),

                       url(r'^searchs/$', views.search_agreement, name='search_agreement'),

                       url(r'^detail/$', views.detail_agreement_ajax, name='detail_agreement_ajax'),

                       url(r'^export$', views.export_agreement, name='export_agreement'),

                       url(r'^searchvalid/$', views.search_valid, name='search_valid'),

                       url(r'^searchall/$', views.search_all, name='search_all'),
                       ]
