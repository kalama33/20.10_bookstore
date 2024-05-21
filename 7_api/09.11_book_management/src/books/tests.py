from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
import pytest
from .models import Book

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def create_book(db):
    return Book.objects.create(title='Test Book', author='Test Author', published_date='2023-01-01')

def test_unauthenticated_user_can_read_books(api_client, create_book):
    response = api_client.get('/books/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

def test_authenticated_user_can_create_book(api_client, create_user):
    api_client.force_authenticate(user=create_user)
    response = api_client.post('/books/', {'title': 'New Book', 'author': 'New Author', 'published_date': '2023-01-01'})
    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.filter(title='New Book').exists()
    
def test_authenticated_user_can_update_book(api_client, create_user, create_book):
    api_client.force_authenticate(user=create_user)
    book_id = create_book.id
    response = api_client.put(f'/books/{book_id}/', {'title': 'Updated Book', 'author': 'Updated Author', 'published_date': '2023-01-01'})
    assert response.status_code == status.HTTP_200_OK
    assert Book.objects.get(id=book_id).title == 'Updated Book'

def test_authenticated_user_can_delete_book(api_client, create_user, create_book):
    api_client.force_authenticate(user=create_user)
    book_id = create_book.id
    response = api_client.delete(f'/books/{book_id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Book.objects.filter(id=book_id).exists()


# Create your tests here.
