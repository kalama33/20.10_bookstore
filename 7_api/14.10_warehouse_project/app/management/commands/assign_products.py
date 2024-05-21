from django.core.management.base import BaseCommand
from app.models import Product, Warehouse #
import requests
import random

class Command(BaseCommand):
    help = 'Assigns products to warehouses randomly'

    def handle(self, *args, **kwargs):
        products = fetch_product_data()

        for product in products:
            # Aquí, podrías crear un nuevo objeto Product en tu DB
            name = product['title']
            price = product['price']
            # Elige un almacén al azar
            warehouse = Warehouse.objects.order_by('?').first()

            new_product = Product(name=name, price=price, warehouse=warehouse)
            new_product.save()

        self.stdout.write(self.style.SUCCESS('Successfully assigned products'))