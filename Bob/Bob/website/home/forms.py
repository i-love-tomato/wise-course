#!/usr/bin/env python
# coding:utf-8

from django import forms
from .models import Meeting
from login.models import UserProfile
from django.contrib.auth.models import User


class MeetingForm(forms.ModelForm):
    meetingdate0 = forms.DateField(widget=forms.SelectDateWidget)
    introduction0 = forms.CharField(widget=forms.Textarea)
    # starttime0 = forms.TimeField(widget=forms.TimeWidget)
    # introduction = forms.CharField(widget)

    class Meta:
        model = Meeting
        # fields = ("meetingname", "meetingdate", "starttime", "endtime", "place", "introduction", "publisher")
        fields = ("meetingname", "meetingdate", "starttime", "endtime", "place", "theme", "introduction")
    # meetingdate = forms.DateField(label="meetingdate", widget=forms.DateInput)