from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import AuthenticatedUserMixin

# Create your views here.
class AfterPage(AuthenticatedUserMixin, TemplateView):
    template_name = 'after.html'
    

def home(request):
    return render(request, 'home.html')    
   