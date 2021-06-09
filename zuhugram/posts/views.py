from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from posts.models import Post
from django.urls import reverse	
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
class PostList(ListView):
	model = Post

class PostCreate(CreateView):
	model = Post
	fields = ['image', 'description','author']
	success_url = '/'

