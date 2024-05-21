from django.shortcuts import render
from django.http import HttpResponse
from .data import POSTS

def homePageView(request):
    return HttpResponse("POSTS")



# Create your views here.
