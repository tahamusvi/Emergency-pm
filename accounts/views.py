from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
from django.contrib.auth.views import LoginView
from django.views.generic import (
            ListView,
            CreateView,
            UpdateView,
            DeleteView,
            DetailView,)
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,redirect
from .forms import *
from  django.contrib.auth import authenticate
from  django.contrib.auth import logout as lgo
from  django.contrib.auth import login as lg
from django.contrib import messages
from .models import User
#----------------------------------------------------------------------------------------------
def logout(request):
    lgo(request)
    return redirect('accounts:login')
#----------------------------------------------------------------------------------------------
def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                lg(request,user)
                messages.success(request,'you logged in successfully','success')
                return redirect('epm:home')
            else:
                messages.error(request,'username or password is wrong','alert')
    else:
        form = UserLoginForm
    return render(request,"accounts/Login.html",{'form':form})
#----------------------------------------------------------------------------------------------
def SignUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if(cd['password']==cd['password2']):
                user = User(username=cd['username'])
                user.set_password(cd['password'])
                user.save()
                lg(request,user)
                return redirect('words:panel')
            else:
                messages.error(request,'username or password is wrong','alert')
    else:
        form = UserSignUpForm
    return render(request,"accounts/signup.html",{'form':form})

#----------------------------------------------------------------------------------------------
