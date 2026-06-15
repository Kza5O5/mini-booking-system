from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from items.models import Item


class ItemTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        response = self.client.post(
            "/api/login/",
            {
                "username": "testuser",
                "password": "password123"
            },
            format="json"
        )

        token = response.data["access"]

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {token}"
        )

    def test_create_item(self):
        response = self.client.post(
            "/api/items/",
            {
                "name": "Laptop Booking",
                "description": "Dell XPS"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Item.objects.count(),
            1
        )