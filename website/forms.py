from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import UserModel
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label = "", widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label = "", max_length = 50 ,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label = "", max_length = 50 ,widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}))