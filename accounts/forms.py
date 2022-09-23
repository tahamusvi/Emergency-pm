from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

#------------------------------------------------------------------------------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


    def __init__(self, *arg,**kwargs):
        user = kwargs.pop('user')

        super(ProfileForm, self).__init__( *arg,**kwargs)
        if not user.is_staff:
            self.fields['username'].disabled = True
            self.fields['username'].help_text = False
#------------------------------------------------------------------------------------------------
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
#------------------------------------------------------------------------------------------------
class UserSignUpForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=40)
    password2 = forms.CharField(max_length=40)
#------------------------------------------------------------------------------------------------
