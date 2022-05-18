from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hellopage(request):
    return HttpResponse("Hello, THIS IS HELLO PAGE")

def youarenotPrepared(request):
    return HttpResponse("You are not Prepared!")