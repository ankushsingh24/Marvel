from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>This is the Home page</h1>')


def about(request):
    return HttpResponse('<h1>This is the About page</h1>')


def services(request):
    return HttpResponse('<h1>This is the Services page</h1>')


def contact(request):
    return HttpResponse('<h1>This is the Contact page</h1>')
