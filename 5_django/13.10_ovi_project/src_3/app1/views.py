from django.shortcuts import render

# Create your views here.

def homepage_app1(request):
    return render(request, 'home_1.html')

def about_app1(request):
    return render(request, 'about_1.html')

def contact_app1(request):
    return render(request, 'contact_1.html')