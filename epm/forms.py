from django import forms
from .models import *

class EpmForm(forms.ModelForm):
    class Meta:
        model = Epm
        fields = ['text', ]
