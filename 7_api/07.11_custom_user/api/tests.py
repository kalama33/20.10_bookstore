from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Profile

class ProfileAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.profile_url = reverse('profile-list')

    def test_get_profiles(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_user_cannot_create_profile(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/profiles/', data={'name': 'John Doe'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(Profile.objects.filter(name='John Doe').exists())

    def test_unauthenticated_user_cannot_update_profile(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(f'/api/profiles/{self.user.id}/', data={'name': 'Updated Name'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(Profile.objects.filter(name='Updated Name').exists())

    def test_unauthenticated_user_cannot_delete_profile(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(f'/api/profiles/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_authenticated_user_can_update_own_profile(self):
        response = self.client.put(f'/api/profiles/{self.user.id}/', data={'name': 'Updated Name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Profile.objects.get(user=self.user).name, 'Updated Name')

    def test_authenticated_user_can_delete_own_profile(self):
        response = self.client.delete(f'/api/profiles/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Profile.objects.filter(user=self.user).exists())


