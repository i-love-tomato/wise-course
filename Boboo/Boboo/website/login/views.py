from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserphotoForm
from . import models
from django.contrib.auth import views as auth_views
from django.contrib import messages

def user_login(request):
    # if request.session.get('is_login',None):
    #     return redirect('zhuce')
    error_msg = ""
    if request.method == "POST":
        # auth_views.LoginView.as_view(template_name='login/login.html')
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('/home/mlist')
            else:
                error_msg = '用户名或密码错误'
                login_form = LoginForm()
                return render(request, 'login/login.html', {'error_msg': error_msg}, {"form": login_form})
                #return redirect("Sorry. Byebye")
        else:
            error_msg = '用户不存在'
            #return HttpResponse("Invalid login1")
            login_form = LoginForm()
            return render(request, 'login/login.html', {'error_msg': error_msg}, {"form": login_form})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login/login.html", {"form": login_form})


def user_register(request):
    if request.method == "GET":
        register_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        userphoto_form = UserphotoForm()
        return render(request, "login/register.html", {"form": register_form, "profile": userprofile_form,  "photo": userphoto_form})

    elif request.method == "POST":
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userphoto_form = UserphotoForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            if userprofile_form.is_valid():
                new_profile = userprofile_form.save(commit=False)
                new_profile.user = new_user
                new_profile.email = request.POST['email']
                new_profile.save()
                if userphoto_form.is_valid():
                    new_photo = userphoto_form.save(commit=False)
                    new_photo.id = new_user
                    new_photo.image = request.FILES.get('image')
                    new_photo.save()
                    messages.add_message(request, messages.SUCCESS, '注册成功‘')
                    return redirect('/login/')
                else:
                    messages.add_message(request, messages.SUCCESS, '注册成功‘')
                    return redirect('/login/')
            else:
                messages.add_message(request, messages.WARNING, '邮箱输入不能为空!')
                return redirect('/login/register')
        else:
            messages.add_message(request, messages.WARNING, '两次密码输入不匹配!')
            return redirect('/login/register')



