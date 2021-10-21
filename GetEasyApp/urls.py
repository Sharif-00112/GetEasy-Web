from django.urls import path, include

from GetEasyApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getservice/<str:sid>/', views.getservices, name='getservice'),
    path('all_services/', views.all_services, name="all_services"),
    path('service_details/<str:sid>/', views.service_details, name="service_details"),
    path('make_appointment/', views.make_appointment, name="make_appointment"),
    path('faq/', views.faq, name="faq")
]
