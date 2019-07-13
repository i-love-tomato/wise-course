from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeetingForm
from django.contrib.auth.models import User
from login.models import UserProfile

@login_required()

def user_home(request):
    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, "home/home.html", {"user": request.user, "userprofile": userprofile})

def user_bianji(request):
    if request.method == "GET":
        return render(request, "home/modification.html")

def user_fabuchuangjian(request):
    if request.method == "GET":
        # meeting_form = MeetingForm()
        return render(request, "home/publish.html")#, {"meetingform":meeting_form})

    # elif request.method == "POST":
    #     meeting_form = MeetingForm()
    #     if meeting_form.is_valid():

def user_createmeet(request):
    if request.method == "GET":
        meeting_form = MeetingForm()
        return render(request, "home/mcreate.html", {"meetingform": meeting_form})
    elif request.method == "POST":
        meeting_form = MeetingForm(request.POST)
        if meeting_form.is_valid():
            new_meeting=meeting_form.save(commit=False)
            new_meeting.save()
            return redirect('/home/fabuchuangjian')
        else:
            return render(request, "home/mlist.html")


def user_fabuguanli(request):
    if request.method == "GET":
        return render(request, "home/manage.html")

def user_huiyiliebiao(request):
    if request.method == "GET":
        return render(request, "home/mlist.html")

def user_huiyiyaoqing(request):
    if request.method == "GET":
        return render(request, "home/invitation.html")