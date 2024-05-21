from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Interaction(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    date = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return f"From {self.from_user} to {self.to_user} on {self.date}"