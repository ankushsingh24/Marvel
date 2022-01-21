from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('<h1>This is the Home page</h1>')


def avengers(request):
    return render(request, 'avengers.html')
    # return HttpResponse('<h1>This is the Avengers page</h1>')


def phaseI(request):
    return render(request, 'phaseI.html')
    # return HttpResponse('<h1>This is the Phase I page</h1>')


def phaseII(request):
    return render(request, 'phaseII.html')


def phaseIII(request):
    return render(request, 'phaseIII.html')


def phaseIV(request):
    return render(request, 'phaseIV.html')


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('<h1>This is the Contact page</h1>')
