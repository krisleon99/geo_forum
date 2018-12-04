# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.agreementgesp',),
}

urlpatterns = [
                       url(r'^$', views.list_agreementgesp, name='list_agreementgesp'),

                       url(r'^conacyt_fund/$', views.list_conacyt_fund, name='list_conacyt_fund'),

                       url(r'^accomplishment/$', views.list_accomplishment, name='list_accomplishment'),

                       url(r'^peoplecontac/$', views.list_peoplecontac, name='list_peoplecontac'),

                       url(r'^(?P<id_agreement>\d+)/?$', views.detail_agreementgesp, name='detail_agreementgesp'),

                       url(r'^upload/$', views.upload_agreementgesp, name='upload_agreementgesp'),

                       url(r'^uploadesp/$', views.upload_agreementgesp_esp, name='upload_agreementgesp_esp'),

                       url(r'^conacyt_fund/upload/$', views.upload_conacyt_fund, name='upload_conacyt_fund'),

                       url(r'^accomplishment/upload/$', views.upload_accomplishment, name='upload_accomplishment'),

                       url(r'^peoplecontac/upload/$', views.upload_peoplecontac, name='upload_peoplecontac'),

                       url(r'^update/(?P<id_agreement>\d+)$', views.update_agreementgesp, name='update_agreementgesp'),

                       url(r'^updateesp/(?P<id_agreement>\d+)$', views.update_agreementgesp_esp, name='update_agreementgesp_esp'),

                       url(r'^resourceseesp/(?P<id_agreement>\d+)$', views.resourcese_agreementgesp, name='resourcese_agreementgesp'),

                       url(r'^conacyt_fund/update/(?P<id_cf>\d+)$', views.update_conacyt_fund, name='update_conacyt_fund'),

                       url(r'^accomplishment/update/(?P<id_accom>\d+)$', views.update_accomplishment, name='update_accomplishment'),

                       url(r'^peoplecontac/update/(?P<id_peop>\d+)$', views.update_peoplecontac, name='update_peoplecontac'),

                       url(r'^save_progress/$', views.save_progress, name='save_progress'),

                       url(r'^upload_accom/(?P<id_agreement>\d+)/?$', views.upload_accomplishment_agreement, name='upload_accomplishment_agreement'),

                       url(r'^remove/(?P<id_agreement>\d+)$', views.remove_agreementgesp, name='remove_agreementgesp'),

                       ]
