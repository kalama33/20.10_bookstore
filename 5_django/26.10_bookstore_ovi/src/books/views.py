from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    
class ListView(TemplateView):
    template_name = 'list_of_books.html'
    

