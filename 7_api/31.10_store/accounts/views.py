from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    success_url = reverse_lazy('landing')
    template_name = 'signup.html'
    form_class = UserCreationForm
