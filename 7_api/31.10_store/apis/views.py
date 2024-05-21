from django.shortcuts import render
from rest_framework import generics
from plants.models import Plant
from .serializers import PlantSerializer

class PlantAPIView(generics.ListAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer