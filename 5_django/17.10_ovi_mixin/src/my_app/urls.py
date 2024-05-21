from django.urls import path
from .views import AfterPage, home

urlpatterns = [
    path('after/', AfterPage.as_view(), name = 'after'),
    path('', home, name = 'home')
    
    
]
 
