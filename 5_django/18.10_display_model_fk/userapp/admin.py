from django.contrib import admin
from .models import Profile # import model Profile from my app

# Register your models here.

admin.site.register(Profile) # registration of Profile's model