from django.core.management.base import BaseCommand
from myapp.models import Product, Warehouse
import random

class Command(BaseCommand):
    help = 'Assigns products to warehouses randomly'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        warehouses = Warehouse.objects.all()

        if not warehouses:
            self.stdout.write(self.style.ERROR('No warehouses available'))
            return

        for product in products:
            warehouse = random.choice(warehouses)
            product.warehouse = warehouse
            product.save()
            self.stdout.write(self.style.SUCCESS(f'Assigned {product.name} to {warehouse.location}'))
