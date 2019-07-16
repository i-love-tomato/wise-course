from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeetingForm
from django.contrib.auth.models import User
from login.models import UserProfile, Photo

@login_required()

def user_home(request):
    userprofile = UserProfile.objects.get(user=request.user)
    photo = Photo.objects.get(id=request.user)
    return render(request, "home/home.html", {"user": request.user, "userprofile": userprofile, "photo": photo})


@login_required(

)
def user_info_revise(request):
    if request.method == "GET":
        return render(request, "home/info_revise.html")


@login_required()

def user_publish(request):
    if request.method == "GET":
        # meeting_form = MeetingForm()
        return render(request, "home/publish.html")#, {"meetingform":meeting_form})

    # elif request.method == "POST":
    #     meeting_form = MeetingForm()
    #     if meeting_form.is_valid():


@login_required()

def user_mcreate(request):
    if request.method == "GET":
        meeting_form = MeetingForm()
        return render(request, "home/mcreate.html", {"meetingform": meeting_form})
    elif request.method == "POST":
        meeting_form = MeetingForm(request.POST)
        if meeting_form.is_valid():
            new_meeting = meeting_form.save(commit=False)
            # new_meeting.meeti ngdate = request.POST['meetingdate']
            new_meeting.starttime = request.POST['starttime']
            new_meeting.endtime = request.POST['endtime']
            new_meeting.meetingdate = meeting_form.cleaned_data['meetingdate0']
            new_meeting.introduction = meeting_form.cleaned_data['introduction0']
            new_meeting.save()
            return redirect('/home/publish')
        else:
            return render(request, "home/mlist.html")


@login_required()

def user_manage(request):
    if request.method == "GET":
        return render(request, "home/manage.html")


@login_required()

def user_mlist(request):
    if request.method == "GET":
        return render(request, "home/mlist.html")


@login_required()

def user_invitation(request):
    if request.method == "GET":
        return render(request, "home/invitation.html")


# @login_required()

# def user_mrevise(request):