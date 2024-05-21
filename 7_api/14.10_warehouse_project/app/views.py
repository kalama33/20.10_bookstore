from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAuthenticated]
