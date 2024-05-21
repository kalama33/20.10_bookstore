from django.core.management.base import BaseCommand
import requests
from myapp.models import Product

class Command(BaseCommand):
    help = 'Fetch and store products from fakestoreapi'

    def handle(self, *args, **kwargs):
        response = requests.get('https://fakestoreapi.com/products')
        if response.status_code == 200:
            products_data = response.json()
            for product_data in products_data:
                Product.objects.create(
                    name=product_data['title'],
                    price=product_data['price'],
                    # Asegúrate de mapear correctamente todos los campos necesarios
                    # de tu modelo Product con los datos de la API
                )
                self.stdout.write(self.style.SUCCESS(f"Product {product_data['title']} added."))
        else:
            self.stdout.write(self.style.ERROR('Error fetching products from the API'))
