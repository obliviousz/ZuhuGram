from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from posts.models import Post
from django.urls import reverse	
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from posts.models import Profile
from django.views.generic import DetailView
class PostList(ListView):
	model = Post

class PostCreate(CreateView):
	model = Post
	fields = ['image', 'description','author']
	success_url = '/'

# class ProfileView(DetailView):
# 	model = Profile
# 	template_name = 'profile/profile_page.html'
# 	def get_context_data(self, *Args, **kwargs):
# 		users = Profile.objects.all()
# 		context = super(ProfileView,self).get_context_data(*args, **kwargs)
# 		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
# 		context["page_user"]=page_user
# 		return context
