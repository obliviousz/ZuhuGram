from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	image = models.ImageField()
	description = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	likes = models.ManyToManyField(User, related_name='blog_post')

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

	def __str__(self):
		return str(self.user)


