from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

# Create your tests here.
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea un usuario
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        # Crea un libro
        cls.book = Book.objects.create(title='A Good Book Title', author='An Author')
        
# tests.py
def test_book_creation(self):
    self.assertEqual(self.book.title, 'A Good Book Title')

def test_book_retrieval(self):
    book_from_db = Book.objects.get(id=self.book.id)
    self.assertEqual(book_from_db.title, 'A Good Book Title')

def test_book_update(self):
    self.book.title = 'An Updated Title'
    self.book.save()
    updated_book = Book.objects.get(id=self.book.id)
    self.assertEqual(updated_book.title, 'An Updated Title')

def test_book_deletion(self):
    book_id = self.book.id
    self.book.delete()
    with self.assertRaises(Book.DoesNotExist):
        Book.objects.get(id=book_id)

def test_str_representation(self):
    self.assertEqual(str(self.book), 'A Good Book Title')

def test_book_get_absolute_url(self):
    self.assertEqual(self.book.get_absolute_url(), f'/book/{self.book.id}/')
