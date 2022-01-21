from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('avengers/', views.avengers, name='avengers'),
    path('phaseI/', views.phaseI, name='phaseI'),
    path('phaseII/', views.phaseII, name='phaseII'),
    path('phaseIII/', views.phaseIII, name='phaseIII'),
    path('phaseIV/', views.phaseIV, name='phaseIV'),
    path('contact/', views.contact, name='contact'),
]
