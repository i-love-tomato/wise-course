#!/usr/bin/env python
# coding:utf-8

from django import forms
from .models import Meeting
from login.models import UserProfile
from django.contrib.auth.models import User

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ("meetingname", "meetingtime", "place", "introduction", "publisher")