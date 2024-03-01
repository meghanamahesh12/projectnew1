from .models import *
from django import forms


class Listform(forms.ModelForm):
    class Meta:
        model=Signin
        fields='__all__'