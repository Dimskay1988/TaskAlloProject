from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from board.models import Announs, ImagePost
from .forms import AnnounsForm
from django.views.generic import DeleteView


def annouce(request):
    result = ImagePost.objects.filter()
    return render(request, 'announcepage.html', context={'ImagePost': result})


def newfilter(request, post=1):
    post_id = post
    result = ImagePost.objects.filter(id=post_id)
    return render(request, 'announcepagedynamic.html', context={'ImagePost': result})


def deleteannounce(request, post):
    post_id = post
    if request.method == 'POST':
        result = Announs.objects.get(id=post_id)
        result.delete()
        return redirect('/announce/')
    else:
        return render(request, "announcepageerror.html")



def createannounce(request):
    error = ''
    if request.method == 'POST':
        form = AnnounsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/announce/')
        else:
            error = 'Неправильное заполнение'
    form = AnnounsForm()
    datanew = {'form': form,
               'error': error
               }
    return render(request, 'announcepagecreate.html', datanew)
