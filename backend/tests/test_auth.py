from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status


class AuthTests(APITestCase):

    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }

        response = self.client.post(
            "/api/register/",
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )

    def test_user_login(self):
        User.objects.create_user(
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

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "access",
            response.data
        )