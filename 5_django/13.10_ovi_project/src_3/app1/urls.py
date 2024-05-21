
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage_app1),
    path('about/', about_app1),
    path('contact/', contact_app1),
]