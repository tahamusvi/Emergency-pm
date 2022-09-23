from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate
from  django.contrib.auth import login as lg
from .models import *
from .forms import *
from django.contrib import messages
from  django.contrib.auth import logout as lgo
#----------------------------------------------------------------------------------------------
def logout(request):
    lgo(request)
    return redirect('accounts:Login')
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
                return redirect('accounts:home')
            else:
                messages.error(request,'username or password is wrong','alert')
    else:
        form = UserLoginForm
    return render(request,"accounts/Login.html",{'form':form})
#----------------------------------------------------------------------------------------------
def home(request):
    if request.method == 'POST':
        form = EpmForm(request.POST)

        if form.is_valid():
            if(request.user.username == 'taha'):
                newEpm = Epm(text = form.cleaned_data['text'],us=True ).save()
            else:
                newEpm = Epm(text = form.cleaned_data['text'],us=False ).save()

            return redirect('accounts:home')




    form = EpmForm()
    user = request.user

    epms = Epm.objects.all()

    return render(request,'accounts/index.html',{'myname':user.username,'form':form,'epms':epms})
