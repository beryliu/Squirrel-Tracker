from django.shortcuts import render
from .models import Squirrel
import random
# Create your views here.


def index(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }

    return render(request, 'sightings/index.html', context)

def map_(request):
    sightings = Squirrel.objects.all()[:50] 
    context = {
            "sightings": sightings
            }
    return render(request, 'sightings/map.html', context) 
