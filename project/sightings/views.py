from django.shortcuts import render
from .models import Squirrel

# Create your views here.


def map_(request):
    Squirres = Squirres.object.all()[:100] 
    context = {
            "Squirres": Squirres
            }
    return render(request, 'sightings/map.html', context) 
