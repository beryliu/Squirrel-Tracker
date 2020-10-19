from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Squirrel
from .forms import Form
import random
import json


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)


def update(request, Squirrel_Unique_ID):
    s = get_object_or_404(Squirrel, pk=Squirrel_Unique_ID)
    form = Form(request.POST or None, instance=s)
    context = {
        'form': form,
    }
    if form.is_valid():
        s = form.save(commit=False)
        s.save()
        return redirect('/sightings/')
    else:
        context = {
            'form': form,
        }
        return render(request, 'sightings/update.html', context)


def add(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/sightings/')
    else:
        form = Form()
        context = {
            'form': form,
        }
        return render(request, 'sightings/add.html', context)



def map_(request):
    sightings = Squirrel.objects.all()[:50] 
    context = {
            "sightings": sightings
            }
    return render(request, 'sightings/map.html', context) 
