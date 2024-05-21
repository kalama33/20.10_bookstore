from django.urls import path
from . import views
from .views import (
PetListView,
PetDetailView,
PetCreateView,
)

urlpatterns = [
path('pet_list/', PetListView.as_view(), name='pet-list'),
path('<int:pk>/', PetDetailView.as_view(), name='pet-detail'),
path('create/', PetCreateView.as_view(), name='pet-create'),
]

