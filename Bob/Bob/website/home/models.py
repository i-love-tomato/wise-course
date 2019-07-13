from django.db import models
from django.utils import timezone
from login.models import UserProfile
# Create your models here.

class Meeting(models.Model):
    meetingname = models.CharField(max_length=100)
    meetingtime = models.DateTimeField()
    place = models.CharField(max_length=50)
    introduction = models.CharField(max_length=400)
    publishtime = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(UserProfile, related_name="meeting_column", on_delete=models.CASCADE)
    user_participation = models.ManyToManyField(UserProfile, related_name="meeting_participation", blank=True)

    class Meta:
        ordering = ['publishtime']


