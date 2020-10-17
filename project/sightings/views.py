from django.shortcuts import render
from .models import Squirrel

# Create your views here.


def map(request):
    Squirres = Squirres.object.all()[:100] 
    context = {
            "Squirres": Squirres
            }
    return render(request, 'map/map.html', context) 
