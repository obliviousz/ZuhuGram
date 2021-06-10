"""zuhugram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from posts.views import PostList, PostCreate
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PostList.as_view(),name='list'),
    path('new/',PostCreate.as_view(),name='new'),
    path('register/',v.register, name="register"),
    path('edit_profile/',v.UserEditView.as_view(), name="edit-profile"),
    path('<int:pk>/edit_profile_photo',v.EditProfilePhotoView.as_view(),name="edit-dp"),
    path('', include("django.contrib.auth.urls")),
    # path('<int:pk>/profile/',ProfileView.as_view(),name='profile_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
