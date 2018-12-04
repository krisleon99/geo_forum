# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import include, url
from . import views

js_info_dict = {
    'packages': ('doc_forum.forum',),
}

urlpatterns = [
               # url(r'^$', views.forum_web, name='forum_web'),
               url(r'^forum/forum_web/$', views.forum_web, name='forum_web'),
               url(r'^upload/$', views.upload_topic, name='upload_topic'),
               url(r'^update/(?P<id_topic>\d+)$', views.update_topic, name='update_topic'),
               url(r'^view/(?P<id_topic>\d+)$', views.view_topic, name='view_topic'),
               url(r'^up_forum/(?P<id_forum>\d+)/(?P<id_topic>\d+)$', views.update_forum, name='update_forum'),
               url(r'^remove/(?P<id_forum>\d+)/(?P<id_topic>\d+)$', views.delete_forum, name='delete_forum'),
               url(r'^save_like_forum/$', views.save_like_forum, name='save_like_forum'),
               url(r'^close/$', views.close_topic, name='close_topic'),
               url(r'^re_tp/(?P<id_topic>\d+)$', views.delete_topic, name='delete_topic'),
               
               ]
