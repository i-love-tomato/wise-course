from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm
from . import models
from django.contrib.auth import views as  auth_views

def user_login(request):
    # if request.session.get('is_login',None):
    #     return redirect('zhuce')

    if request.method == "POST":
        # auth_views.LoginView.as_view(template_name='login/login.html')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/home/huiyiliebiao')
            else:
                return HttpResponse("Sorry. Byebye")
        else:
            return HttpResponse("Invalid login1")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login/login.html", {"form": login_form})


def user_register(request):
    if request.method == "GET":
        register_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "login/register.html", {"form": register_form, "profile": userprofile_form})

    elif request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return redirect('/login')
        else:
            return HttpResponse("sorry")



