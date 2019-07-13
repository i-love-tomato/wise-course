#!/usr/bin/env python
# coding:utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('bianji/', views.user_bianji),
    path('fabuchuangjian/', views.user_fabuchuangjian),
    path('fabuguanli/', views.user_fabuguanli),
    path('huiyiliebiao/', views.user_huiyiliebiao),
    path('huiyiyaoqing/', views.user_huiyiyaoqing),
    path('createmeet/', views.user_createmeet),
]
