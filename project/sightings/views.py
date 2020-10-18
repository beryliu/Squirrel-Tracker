from django.shortcuts import render
from .models import Squirrel
import random
# Create your views here.


def map_(request):
    sightings = Squirrel.objects.all() 
    context = {
            "sightings": sightings
            }
    return render(request, 'sightings/map.html', context) 
