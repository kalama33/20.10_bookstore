from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product, Warehouse

class ProductAPITestCase(APITestCase):

    def test_get_products(self):
        # Agrega código para probar el endpoint GET
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        # Agrega código para probar el endpoint POST
        data = {'name': 'New Product', 'price': 10.99}
        response = self.client.post(reverse('product-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def setUp(self):
        # Crear un producto para las pruebas
        self.product = Product.objects.create(name='Test Product', price=9.99)
        self.url = reverse('product-detail', kwargs={'pk': self.product.pk})
        
    def test_update_product(self):
        # Prueba para actualizar un producto existente
        updated_data = {'name': 'Updated Product', 'price': 15.99}
        response = self.client.put(self.url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        
    
