from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from posts.models import Profile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username","email","password1","password2"]

class EditForm(UserChangeForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	class Meta:
		model = User
		fields = ["username","email","first_name","last_name"]