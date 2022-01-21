from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>This is the Home page</h1>')


def avengers(request):
    return HttpResponse('<h1>This is the Avengers page</h1>')


def phaseI(request):
    return HttpResponse('<h1>This is the Phase I page</h1>')


def contact(request):
    return HttpResponse('<h1>This is the Contact page</h1>')
