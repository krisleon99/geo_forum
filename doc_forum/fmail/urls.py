# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.fmail',),
}

urlpatterns = [
               url(r'^follow/(?P<id_topic>\d+)$', views.follow_forum, name='follow_forum'),
               url(r'^leave/(?P<fmail>\d+)$', views.leave_forum, name='leave_forum'),
               url(r'^follow_us/(?P<id_user>\d+)$', views.follow_user, name='follow_user'),
               url(r'^leave_us/(?P<fmail>\d+)/(?P<id_user>\d+)$',views.leave_user, name='leave_user'),
               url(r'^follow_dim/$', views.follow_dimension, name='follow_dimension'),
               url(r'^leave_dim/(?P<fmail>\d+)$', views.leave_dimension, name='leave_dimension'),
               url(r'^test/$', views.test_email, name='test_email'),
               url(r'^threading/$', views.start_stop_thread, name='start_stop_thread'),

               ]
