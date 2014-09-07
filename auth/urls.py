# -*- coding: utf-8 -*-
__author__ = 'D.Ivanets'
from django.conf.urls import url
import views

urlpatterns = [
    # url(r'^ajax_login/$', views.login),
    url(r'^login/$', views.login),
    url(r'^signup/$', views.signup),
    url(r'^email_conf/(.*)/$', views.email_conf),
    # url(r'^company/edit/(.*)$', None),
    # url(r'^', views.error),
]