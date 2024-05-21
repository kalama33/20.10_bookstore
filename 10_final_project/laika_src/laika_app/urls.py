from django.urls import path
from . import views
from .views import PetProfileListView

urlpatterns = [
    path('pet_list/', PetProfileListView.as_view(), name='pet_list'),
]
