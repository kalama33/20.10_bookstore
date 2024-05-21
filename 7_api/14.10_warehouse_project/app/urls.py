from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, WarehouseViewSet

# Crea un enrutador y registra viewsets con él
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'warehouses', WarehouseViewSet)

# URLs de la API están determinadas automáticamente por el enrutador
urlpatterns = [
    path('', include(router.urls)),
]