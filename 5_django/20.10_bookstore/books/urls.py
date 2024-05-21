from django.urls import path, include
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookCreateView,
    BookDeleteView,
    RegisterView, 
    LoginView, 
    LogoutView,
)

book_patterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
  # Rutas para las vistas de autenticación

auth_patterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
    
urlpatterns = [
    path('', include(book_patterns), name='book_patterns'),      #
    path('auth/', include(auth_patterns), name='auth_patterns'), #
]
