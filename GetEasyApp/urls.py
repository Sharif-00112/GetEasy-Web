from django.urls import path, include

from GetEasyApp import views

urlpatterns = [
    path('', views.home, name="home")
]
