from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'userapp/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'userapp/profile_detail.html'
