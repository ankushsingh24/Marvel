from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('avengers/', views.avengers, name='avengers'),
    path('phaseI/', views.phaseI, name='phaseI'),
    path('contact/', views.contact, name='contact'),
]
