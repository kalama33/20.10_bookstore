from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Pet
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

class PetListView(ListView):
    model = Pet                              
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'                    
    
class PetDetailView(DetailView):
    model = Pet                              
    template_name = 'pets/pet_detail.html'
    context_object_name = 'pets'

class PetCreateView(CreateView):
	model = Pet
	fields = ['user', 'name', 'species','breed', 'age', 'description']
	template_name = 'pets/pet_form.html'
	success_url = reverse_lazy('pet-list')