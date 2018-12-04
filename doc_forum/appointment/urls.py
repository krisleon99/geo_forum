# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.appointment',),
}

urlpatterns = [
               # url(r'^$', views.forum_web, name='forum_web'),
               url(r'^detail_ev/(?P<id_event>\d+)$', views.event_detail, name='event_detail'),
               url(r'^update_ev/(?P<id_event>\d+)$', views.update_event, name='update_event'),
               url(r'^save_ev/$', views.event_save, name='event_save'),
               url(r'^dlt_ev/(?P<id_event>\d+)/?$', views.delete_event, name='delete_event'),

               ]
