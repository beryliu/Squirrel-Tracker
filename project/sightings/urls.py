from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('map/',views.map_, name='map_'),
]
