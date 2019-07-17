#!/usr/bin/env python
# coding:utf-8
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('info_revise/', views.user_info_revise),
    # path('publish/mdelete/', views.user_mdelete, name='mdelete'),
    path('publish/', views.user_publish),
    path('publish/mdelete/', views.user_mdelete, name='mdelete'),
    path('publish/pub_meeting/', views.user_pub_meeting, name='pub_meeting'),
    path('mcreate', views.user_mcreate),
    path('manage/', views.user_manage),
    path('invitation/', views.user_invitation),
    path('mlist/', views.user_mlist),
    re_path('mrevise/(?P<id>\d+)/$', views.user_mrevise, name="mrevise"),
    re_path('manage/see_participant/(?P<id>\d+)/$', views.user_seeparticipant, name="seepar")
]
