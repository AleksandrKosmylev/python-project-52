import unittest
from django.test import Client

from django.test import TestCase
from django.contrib.auth.models import User


"""
class UsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="test_first_name",
            last_name="test_last_name",
            username="test_username",
            )

    def test_create(self):
        user = User.objects.get(first_name="test_first_name")
        self.assertEqual(user.username, "test_username")

    def test_edit(self):
        user = User.objects.get(first_name="test_first_name")
        updated_username = "updated_test_username"
        user.username = updated_username
        self.assertEqual(user.username, updated_username)

    def test_delete(self):
        self.assertIsNotNone(self.user)
        self.user.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user.pk)
"""

class ClientCreateTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_client(self):
        data = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'username': 'test_username',
            "password": 'password',
            "password2": 'password'
        }

        # self.client.get('/users/create/', data=data)
        # response = self.client.post('/users/create/')
        response = self.client.post('/users/create/', data=data)
        print(response.status_code, 'response code', response.content)
        self.assertEqual(response.status_code, 200)