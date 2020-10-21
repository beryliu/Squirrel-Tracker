from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Squirrel
from .forms import Form
import random
import json
from django.db.models import Count
from django.db.models import Avg

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

def stats(request):
    sightings_sum = Squirrel.objects.count()
    sightings_adult = Squirrel.objects.filter(Age='Adult').count()
    sightings_juvenile = Squirrel.objects.filter(Age='Juvenile').count()
    sightings_am = Squirrel.objects.filter(Shift='AM').count()
    sightings_pm = Squirrel.objects.filter(Shift='PM').count()
    sightings_location_G = Squirrel.objects.filter(Location='Ground Plane').count()
    sightings_location_F = Squirrel.objects.filter(Location='Above Ground').count()
    sightings_c_G = Squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    sightings_c_C = Squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    sightings_c_B = Squirrel.objects.filter(Primary_Fur_Color='Black').count()
    sightings_x = Squirrel.objects.aggregate(x=Avg('X'))
    sightings_y = Squirrel.objects.aggregate(y=Avg('Y'))
    context = {
            'sightings_sum':sightings_sum ,
            'sightings_adult':sightings_adult,
            'sightings_juvenile':sightings_juvenile,
            'sightings_am':sightings_am,
            'sightings_pm':sightings_pm,
            'sightings_location_G':sightings_location_G,
            'sightings_location_F':sightings_location_F,
            'sightings_c_B':sightings_c_B,
            'sightings_c_C':sightings_c_C,
            'sightings_c_G':sightings_c_G,
            'sightings_x':sightings_x,
            'sightings_y':sightings_y,

            }
    return render(request,'sightings/stats.html',context)
