from rest_framework import viewsets
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer
from rest_framework import permissions


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
