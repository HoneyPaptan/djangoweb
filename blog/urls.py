from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
 
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("newsletter/", views.newsletter, name="newsletter"),
    path("blogs/", views.blogs, name="blogs"),
    path("blog/<slug:slug>", views.blog, name="blog"),
    path("searched/", views.searched, name="searched"),
]
