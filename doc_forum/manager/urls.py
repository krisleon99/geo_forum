# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import password_change_done
from . import views

js_info_dict = {
    'packages': ('doc_forum.manager',),
}

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^home/$', views.agreement_and_proposal, name='agreement_and_proposal'),
    url(r'^usuario/nuevo$',views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$',views.ingresar, name='ingresar'),
    url(r'^privado/$',views.privado, name='privado'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^usuario/list$',views.user_list, name='user_list'),
    # url(r'^usuario/detail/(?P<id_user>\d+)$',views.user_detail),
    url(r'^usuario/detail/(?P<id_user>\d+)$', views.user_detail, name='user_detail'),
    url(r'^usuario/update/(?P<id_user>\d+)$',views.user_update, name='user_update'),
    url(r'^usuario/delete/(?P<id_user>\d+)$',views.user_delete, name='user_delete'),
    url(r'^usuario/update_basic/(?P<id_user>\d+)$',views.user_update_basic, name='user_update_basic'),
    url(r'^usuario/change_password/$',views.change_password, name='change_password'),
    # url(r'^change/$', 'avatar_change'),
  ]
#urlpatterns += patterns('',
 # (r'^password_change_done/$', 'django.contrib.auth.views.password_change_done','password_change_done'),
#)
