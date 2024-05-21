from django.urls import path
from . import views

urlpatterns = [ 
    path('api/profiles/', views.get_profiles, name='profile-list'),
]