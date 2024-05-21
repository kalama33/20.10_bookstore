from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField()
    need = models.TextField() #
    availability = models.TextField() #
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,) #

    def __str__(self):
        return self.user_name #
    
    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={"pk": self.pk})
    
class Interaction(models.Model): #
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    date = models.DateTimeField()
    message = models.TextField()
        
    def __str__(self):
        return f"From {self.from_user} to {self.to_user} on {self.date}"
