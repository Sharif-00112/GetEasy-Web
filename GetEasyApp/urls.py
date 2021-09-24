from django.urls import path, include

from GetEasyApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getservice/<str:sid>/', views.getservices, name='getservice'),
]
