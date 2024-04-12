# import unittest
# from django.test import Client
from django.test import TestCase
from task_manager.users.models import CustomUser
from django.urls import reverse, reverse_lazy
from . import get_content
from django.utils.translation import gettext_lazy as _


class UsersTest(TestCase):
    fixtures = ['tests/fixtures/db.json']

    def setUp(self):
        self.dump_data = get_content('data.json')

    def test_index_page(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)

        users = CustomUser.objects.all()
        count = users.count()
        self.assertEqual(count, 2)
        self.assertQuerysetEqual(
            response.context['customuser_list'],
            users,
            ordered=False,
        )

    def test_create(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)
        new_user = self.dump_data.get('users').get('new')
        response = self.client.post(reverse_lazy('user_create'), data=new_user,
                                    follow=True)
        created_user = CustomUser.objects.get(id=new_user.get('pk'))
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(created_user.username, new_user.get('username'))
        self.assertContains(response, _('Successfully registered!'))
        # print(CustomUser.objects.all())

    def test_update(self):
        exist_user = CustomUser.objects.get(id=1)
        print(exist_user.last_name, 'exist_user last name')
        updated_user = self.dump_data.get('users').get('updated')
        print(updated_user, 'updated_user!')

        # try to change another user
        print(CustomUser.objects.get(id=2), 'pk2')
        self.client.force_login(user=CustomUser.objects.get(id=2))
        response = self.client.get(reverse('user_update',
                                   args=[exist_user.pk]),
                                   updated_user,
                                   follow=True)
        print(response, 'response')

        not_updated_user = CustomUser.objects.get(id=exist_user.pk)
        print(not_updated_user, 'not_updated_user')

        self.assertRedirects(response, reverse('users_index'))
        self.assertEqual(not_updated_user.last_name, exist_user.last_name)
        self.assertContains(response, _('You cannot edit other users!'))

        # logged in
        self.client.force_login(user=exist_user)
        response = self.client.post(reverse('user_update',
                                            args=[exist_user.pk]),
                                    updated_user,
                                    follow=True)
        updated_user_added = CustomUser.objects.get(id=exist_user.pk)
        print(updated_user_added.last_name, 'updated_user_added')
        self.assertEqual(updated_user_added.last_name, 'Stark')
        self.assertContains(response, _('Successfully updated!'))
        self.assertRedirects(response, reverse('users_index'))

    """
    def test_delete(self):
        exist_user = CustomUser.objects.get(id=1)

        # try to change another user
        self.client.force_login(user=CustomUser.objects.get(id=2))
        response = self.client.get(reverse('user_delete',
                                           args=[exist_user.pk]),
                                   follow=True)

        self.assertRedirects(response, reverse('users_index'))
        self.assertEqual(exist_user.first_name, 'John')
        self.assertContains(response, _("You cannot delete other users!"))

        # logged in
        self.client.force_login(user=exist_user)
        response = self.client.post(reverse('users_delete',
                                            args=[exist_user.pk]),
                                    follow=True)

        self.assertRedirects(response, reverse('users_index'))
        self.assertContains(response, _('Successfully deleted!'))
        with self.assertRaises(ObjectDoesNotExist):
            CustomUser.objects.get(id=1)

    """


"""
user_data = {
    "pk": 3,
    "first_name": "Luke",
    "username": "neo",
    "last_name": "Skywalker",
    "password1": "Parol123",
    "password2": "Parol123"
}
"""
