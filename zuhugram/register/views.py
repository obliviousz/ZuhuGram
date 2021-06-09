from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import RegisterForm,EditForm
from django.views import generic
from django.urls import reverse_lazy
from posts.models import Profile
# Create your views here.

def register(response):
	if response.method =="POST":
		form = RegisterForm(response.POST)
		print(form.errors)
		if form.is_valid():
			form.save()
		return redirect("/")
	else:
		form = RegisterForm()

	return render(response, "register/register.html",{"form": form})


class UserEditView(generic.UpdateView):
	form_class= EditForm
	template_name='registration/edit_profile.html'
	sucess_url = '/'
	def get_success_url(self):
		return ('/')

	def get_object(self):
		return self.request.user

class EditProfilePhotoView(generic.UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_photo.html'
	fields = ['profile_pic']
	def get_success_url(self):
		return ('/')