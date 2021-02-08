from django import forms
from .models import *
class imageform(forms.ModelForm):
    class Meta:
        model =image
        fields=['cid','name','address','city','category','mobile','prize','hotel_Main_Img']


