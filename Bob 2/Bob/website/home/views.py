from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeetingForm, PersonalPhotoForm, PersonalForm
from django.contrib.auth.models import User
from login.models import UserProfile, Photo
from .models import Meeting
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@login_required()
def user_home(request):
    userprofile = UserProfile.objects.get(user=request.user)
    photo = Photo.objects.get(id=request.user)
    return render(request, "home/home.html", {"user": request.user, "userprofile": userprofile, "photo": photo})

@login_required()
def user_info_revise(request):
    #user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    photo = Photo.objects.get(id=request.user)

    if request.method == "POST":
        #email_form = EmailForm(request.POST)
        personal_form = PersonalForm(request.POST)
        personalphoto_form = PersonalPhotoForm(request.POST,request.FILES)
        if personal_form.is_valid() * personalphoto_form.is_valid():
           # email_cd = email_form.cleaned_data
            personal_cd = personal_form.cleaned_data
            personalphoto_cd = personalphoto_form.cleaned_data

            userprofile.realname = personal_cd['realname']
            userprofile.phone = personal_cd['phone']
            userprofile.birth = personal_cd['birth']
            userprofile.company = personal_cd['company']
            userprofile.position = personal_cd['position']
            userprofile.email = personal_cd["email"]
            #user.email = email_cd['email']
            if(personalphoto_cd['image']):
                photo.image = personalphoto_cd['image']

             # user.save()
            userprofile.save()
            photo.save()
        return redirect('/home')
    else:
       # email_form = EmailForm(initial={"email":user.email})
        personal_form = PersonalForm(initial={"realname":userprofile.realname,"phone":userprofile.phone, \
                                              "birth":userprofile.birth, "company":userprofile.company, \
                                              "position":userprofile.position,"email":userprofile.email})
        #photo = Photo.objects.get(id=request.user)
        personalphoto_form = PersonalPhotoForm(initial={"image":photo.image})
        return render(request, "home/info_revise.html",
                      {"personal_form": personal_form, "personalphoto_form": personalphoto_form,"photo":photo})



@login_required()

def user_publish(request):
    if request.method == "GET":
        meetings = Meeting.objects.filter(publisher=request.user)
        # meeting_form = MeetingForm()
        # return render(request, "home/publish.html")
        return render(request, "home/publish.html", {"meetings": meetings})

    # elifrequest.method == "POST":
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
            new_meeting.publisher = request.user
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


@login_required()

def user_mrevise(request, id):
    if request.method == "GET":
        post = get_object_or_404(Meeting, id=id)  #传递默认值
        meetingform = MeetingForm(instance=post)
        meetingform.meetingdate0 = meetingform['meetingdate']
        meetingform.introduction0 = meetingform['introduction']
        return render(request, "home/mrevise.html", {"meetingform": meetingform})

    elif request.method == "POST":
        meeting = Meeting.objects.get(id=id)
        meetingform = MeetingForm(request.POST)
        if meetingform.is_valid():
            meeting.meetingname = meetingform.cleaned_data['meetingname']
            meeting.meetingdate = meetingform.cleaned_data['meetingdate0']
            meeting.starttime = request.POST['starttime']
            meeting.endtime = request.POST['endtime']
            meeting.place = meetingform.cleaned_data['place']
            meeting.introduction = meetingform.cleaned_data['introduction0']
            meeting.save()
            return redirect('/home/publish')
        else:
            return render(request, "home/mlist.html")


@login_required()
@csrf_exempt
@require_POST

def user_mdelete(request):
    meeting_id = request.POST["meeting_id"]
    try:
        meeting = Meeting.objects.get(id=meeting_id)
        meeting.delete()
        return redirect('/home/publish')
    except:
        return HttpResponse("无此会议")