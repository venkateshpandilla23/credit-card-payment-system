from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Card


class CardTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='carduser',
            email='carduser@example.com',
            password='TestPassword123'
        )

        self.client.force_authenticate(
            user=self.user
        )

    def test_create_card(self):
        response = self.client.post(
            '/api/cards/',
            {
                'card_type': 'CREDIT',
                'masked_card': '**** **** **** 1234',
                'last_four': '1234',
                'card_holder_name': 'Test User',
                'expiry_month': 12,
                'expiry_year': 2030
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Card.objects.filter(
                user=self.user,
                last_four='1234'
            ).exists()
        )

    def test_delete_card(self):
        card = Card.objects.create(
            user=self.user,
            card_type='CREDIT',
            masked_card='**** **** **** 5678',
            last_four='5678',
            card_holder_name='Test User',
            expiry_month=12,
            expiry_year=2030
        )

        response = self.client.delete(
            f'/api/cards/{card.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Card.objects.filter(id=card.id).exists()
        )