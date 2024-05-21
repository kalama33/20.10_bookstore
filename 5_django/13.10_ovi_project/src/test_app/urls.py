
from django.urls import path
from .views import homepage_2

urlpatterns = [
    
    path('', homepage_2, name = 'home_2') #
]
