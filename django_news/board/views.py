from django.http import HttpResponse
from django.shortcuts import render
from board.models import Announs

def annouce(request):
    result = Announs.objects.filter()
    return render(request, 'announcepage.html', context={'Announs': result})

