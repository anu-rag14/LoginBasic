from django import forms
from .models import login

class PostForm(forms.Form):
	name =forms.CharField(max_length=120)
	number=forms.CharField(max_length=10)
	otp=forms.CharField(max_length=6) 
