# from django.contrib import admin
from django.urls import path
from .views import home, post_list

urlpatterns = [
    path('', home),
    path('post/', post_list, name= 'posts'),
]
