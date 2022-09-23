from django.shortcuts import render,redirect
from .models import *
from .forms import *


def home(request):
    if request.method == 'POST':
        form = EpmForm(request.POST)

        if form.is_valid():
            if(request.user.username == 'taha'):
                newEpm = Epm(text = form.cleaned_data['text'],us=True ).save()
            else:
                newEpm = Epm(text = form.cleaned_data['text'],us=False ).save()

            return redirect('epm:home')




    form = EpmForm()
    user = request.user

    epms = Epm.objects.all()

    return render(request,'epm/index2.html',{'myname':user.username,'form':form,'epms':epms})
