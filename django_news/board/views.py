from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from board.models import Announs
from .forms import AnnounsForm
from django.views.generic import DeleteView


def annouce(request):
    result = Announs.objects.filter()
    return render(request, 'announcepage.html', context={'Announs': result})


def newfilter(request, post=1):
    post_id = post
    result = Announs.objects.filter(id=post_id)
    return render(request, 'announcepagedynamic.html', context={'Announs': result})


def deleteannounce(request, post):
    post_id = post
    result = Announs.objects.get(id=post_id)
    result.delete()
    return redirect('/announce')


def createannounce(request):
    error = ''
    if request.method == 'POST':
        form = AnnounsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/announce')
        else:
            error = 'Неправильное заполнение'
    form = AnnounsForm()
    datanew = {'form': form,
               'error': error
               }
    return render(request, 'announcepagecreate.html', datanew)
