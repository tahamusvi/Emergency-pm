from django.shortcuts import render,redirect
from .models import *
from .forms import *


def home(request):
    if request.method == 'POST':
        form = EpmForm(request.POST)

        if form.is_valid():
            newEpm = Epm(text = form.cleaned_data['text'],sender=request.user,receiver =request.user ).save()
            return redirect('epm:home')
        return home(request)


    else:
        form = EpmForm()
        user = request.user
        return render(request,'epm/index.html',{'myname':user.username,'form':form})
