from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class AuthTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.signup_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'name': 'testname'
        }
        cls.login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }


    def test_signup(self):
        response = self.client.post(reverse('signup'), self.signup_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertTrue(User.objects.filter(username='testuser').exists())


    def test_login(self):
        self.client.post(reverse('signup'), self.signup_data, format='json')
        response = self.client.post(reverse('login'), self.login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
