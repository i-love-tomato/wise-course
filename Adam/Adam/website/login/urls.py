#!/usr/bin/env python
# coding:utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('zhuce/', views.user_register, name='user_register'),

]

