from django.db import models
from django.utils import timezone
from login.models import UserProfile
# Create your models here.


class Meeting(models.Model):
    meetingname = models.CharField(max_length=100)
    meetingdate = models.DateField(blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True)
    theme = models.CharField(max_length=50, blank=True)
    introduction = models.CharField(max_length=400, blank=True)
    publishtime = models.DateTimeField(auto_now_add=True)
    # publisher = models.ForeignKey(UserProfile, related_name="meeting_column", on_delete=models.CASCADE)
    user_participation = models.ManyToManyField(UserProfile, related_name="meeting_participation", blank=True)
    # finished = models.BooleanField

    class Meta:
        ordering = ['publishtime']


