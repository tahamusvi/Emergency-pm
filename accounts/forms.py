from django import forms
from .models import *

#------------------------------------------------------------------------------------------------
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
#------------------------------------------------------------------------------------------------
class EpmForm(forms.ModelForm):
    class Meta:
        model = Epm
        fields = ['text', ]
