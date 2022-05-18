from django.http import HttpResponse
from django.shortcuts import render


def postes(request, post=1):
    return render(request, 'postpage.html', {'post':post})

def aboutproject(request):
    return render(request, 'aboutproject.html')

def redsquad(request):
    return render(request, 'redsquad.html')

def firstpage(request):
    return render(request, 'firstpage.html')

