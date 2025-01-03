from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),  # Add a path for the map
]
