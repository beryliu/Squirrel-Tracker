from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'sightings'

urlpatterns =[
    path('sightings/', views.index, name='index'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/<Squirrel_Unique_ID>/', views.update, name='update'),
    path('map/',views.map_, name='map_'),
]
