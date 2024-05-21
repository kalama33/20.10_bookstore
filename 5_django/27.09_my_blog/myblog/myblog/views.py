from django.shortcuts import render
from django.http import HttpResponse
from .data import POSTS

# Create your views here.

def list_posts(request):
    output = "\n".join([f"Title: {post['title']}\nContent: {post['content']}\n" for post in POSTS])
    return HttpResponse(output, content_type="text/plain")
