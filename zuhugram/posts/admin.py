from django.contrib import admin
from posts.models import Post,Profile
# Register your models here.

admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Profile)