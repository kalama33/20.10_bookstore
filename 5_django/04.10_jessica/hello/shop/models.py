from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    stock = models.PositiveIntegerField()
