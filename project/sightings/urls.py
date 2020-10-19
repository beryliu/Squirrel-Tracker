from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns =[
    path('sightings/', views.index, name='index'),
    path('map/',views.map_, name='map_'),
]
