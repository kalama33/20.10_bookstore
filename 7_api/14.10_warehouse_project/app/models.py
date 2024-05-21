from django.db import models
from django.contrib.auth.models import User

class Warehouse(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)



# Create your models here.
