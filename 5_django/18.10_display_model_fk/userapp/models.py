from django.db import models
from django.contrib.auth.models import User # authentication modul

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #to eliminate related field
    bio = models.CharField(max_length=255)
    
    def __self__(self):
        return self.user.username
    
    



