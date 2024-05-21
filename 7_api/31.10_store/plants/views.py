from django.shortcuts import render
from django.urls import reverse_lazy
from .mixins import AuthenticatedUserMixin, AuthenticatedStaffMixin

# Create your views here.

from .models import Plant
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
)

class PlantListView(AuthenticatedUserMixin, ListView):
    model = Plant
    template_name = 'plants/plant_list.html'
    context_object_name = 'plants'
    
class PlantDetailView(AuthenticatedUserMixin, DetailView):	
    model = Plant
    template_name = 'plants/plant_detail.html'
    context_object_name = 'plant'
 
class PlantCreateView(AuthenticatedStaffMixin, CreateView):	
    model = Plant
    fields = ['title', 'description', 'price']
    template_name = 'plants/plant_form.html'
    success_url = reverse_lazy('plant-list')
 
class PlantUpdateView(AuthenticatedStaffMixin, UpdateView):	
    model = Plant
    fields = ['title', 'description', 'price']
    template_name = 'plants/plant_edit.html'

    def get_success_url(self):
	    return reverse_lazy('plant-detail', kwargs={'pk': self.object.pk})

class PlantDeleteView(AuthenticatedStaffMixin, DeleteView):	
    model = Plant
    template_name = 'plants/plant_delete.html'
    success_url = reverse_lazy('plant-list')