from django.urls import path
from . import views

urlpatterns = [
    path('practice/', views.practice_view, name = 'practice_view')
]