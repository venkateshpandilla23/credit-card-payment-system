from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationTests(APITestCase):

    def test_user_registration(self):
        response = self.client.post(
            '/api/auth/register/',
            {
                'username': 'testuser',
                'email': 'testuser@example.com',
                'password': 'TestPassword123'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            User.objects.filter(username='testuser').exists()
        )

    def test_user_login(self):
        User.objects.create_user(
            username='loginuser',
            email='login@example.com',
            password='TestPassword123'
        )

        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'loginuser',
                'password': 'TestPassword123'
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_profile_requires_authentication(self):
        response = self.client.get('/api/auth/profile/')

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )