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
            "password1": 'password',
            "password2": 'password',
            "password": 'password',
        }

        # user = User.objects.get(username='test_username')
        # print(user.id)
        # user.delete()

        request_create = self.client.post('/users/create/', data=data, follow=True)
        # Check if response works properly
        self.assertEqual(request_create.status_code, 200)
        # Check if response redirect to  proper url
        user = User.objects.get(username='test_username')
        self.assertEqual(request_create.redirect_chain, [('/login/', 302)])
        # Check if user added to database
        self.assertEqual(user.username, data['username'])

    def test_delete_client(self):

        data = {
            'username': 'test_username',
            "password": 'password',
        }
        # Loggin in
        request_login = self.client.post('/login/', data=data, follow=True)
        self.assertEqual(request_login.status_code, 200)
        user = User.objects.get(username='test_username')
        # delete user
        request_delete = self.client.post(f'/users/{user.id}/delete/', follow=True)
        self.assertEqual(request_delete.status_code, 200)
        # Check if response redirect to  proper url
        self.assertEqual(request_delete.redirect_chain, [('/users/', 302)])
        # Check if user deleted to database
        self.assertNotEqual(request_delete, user)

"""
    def test_update_client(self):

        data_new = {
            'first_name': 'test_first_name11',
            'last_name': 'test_last_name11',
            'username': 'test_username11',
            "password1": 'password11',
            "password2": 'password11',
            "password": 'password11',
        }

        user = User.objects.get(username='test_username')
        print(user.id, "user.idd")
        request_upgrade = self.client.post(f'/users/{user.id}/update/',data=data_new)
        # print(request_upgrade.redirect_chain)
        self.assertEqual(user.username, data_new['username'])
        print(user.username, "user_new")
        self.assertEqual(request_upgrade.status_code, 302)
        # self.assertEqual(request_upgrade.redirect_chain, [('/login/', 302)])
"""
