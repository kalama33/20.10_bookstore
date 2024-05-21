from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Article

# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'myapp/article_form.html'
    fields = ['title', 'content']
    

