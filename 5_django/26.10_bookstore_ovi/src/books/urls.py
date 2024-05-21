from django.urls import path
from .views import HomeView, ListView

urlpatterns = [
    path('', HomeView.as_view()),
    path('list', ListView.as_view())
]