#!/usr/bin/env python
# coding:utf-8
from django.urls import path
from . import views
from django.contrib.auth import views as  auth_views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    #path('zhuce/', auth_views.LoginView.as_view(template_name='login/login.html'))
    path('zhuce/', views.user_register, name='user_register'),
]

