from django.shortcuts import render

# Create your views here.

def homepage_app2(request):
    return render(request, 'home_2.html')
