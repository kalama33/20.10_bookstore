from django.views.generic import ListView, DetailView
from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = "home.html"
    
class ProfileDetailView(DetailView): # new
    model = Profile
    template_name = "profile_detail.html"