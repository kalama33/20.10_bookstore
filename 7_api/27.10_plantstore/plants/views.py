from django.shortcuts import render
from django.views.generic import ListView
from .models import Plant
# Create your views here.

class PlantListView(ListView):
    template_name="plant_list.html"
    model=Plant