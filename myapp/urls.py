from myapp.models import User
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home),
    path('users', views.UserList.as_view()),
]
