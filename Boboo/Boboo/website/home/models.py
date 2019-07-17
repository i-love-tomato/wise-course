from django.db import models
from django.utils import timezone
from login.models import UserProfile, User
from django.urls import reverse
# Create your models here.


class Meeting(models.Model):
    meetingname = models.CharField(max_length=100)
    meetingdate = models.DateField(blank=True, null=True)
    starttime = models.TimeField(blank=True, null=True)
    endtime = models.TimeField(blank=True, null=True)
    startdatetime = models.DateTimeField(blank=True, null=True)
    enddatetime = models.DateTimeField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True)
    theme = models.CharField(max_length=50, blank=True)
    introduction = models.CharField(max_length=400, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    publisher = models.ForeignKey(User, related_name="meeting_column", on_delete=models.CASCADE, blank=True, null=True)
    published = models.BooleanField(default=False)
    user_invitation = models.ManyToManyField(User, related_name="meeting_invitation", blank=True)
    user_participation = models.ManyToManyField(User, related_name="meeting_participation", blank=True)


    class Meta:
        ordering = ['create_time']

    def get_revise_url(self):
        return reverse("mrevise", args=[self.id])

    def get_see_paticipant_url(self):
        return reverse("seepar", args=[self.id])

    def get_info_url(self):
        return reverse()


