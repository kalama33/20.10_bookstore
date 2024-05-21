from .models import PetProfile
from django.views.generic import (
    ListView,
    DetailView,
)

class PetProfileListView(ListView):
    model = PetProfile                              
    template_name = 'laika_app/templates/pet_list.html'
    context_object_name = 'pets'                    
    
class PetProfileDetailView(DetailView):
    model = PetProfile                              
    template_name = 'laika_app/templates/pet_detail.html'
    context_object_name = 'pets'
