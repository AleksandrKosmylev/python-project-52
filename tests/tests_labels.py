from django.core.exceptions import ObjectDoesNotExist
from task_manager.labels.models import Labels
from django.urls import reverse
from task_manager.users.models import CustomUser
from tests.test_auth import AuthTestCase
from . import get_content
from django.utils.translation import gettext_lazy as _


class LabelsTestCase(AuthTestCase):
    fixtures = ['tests/fixtures/db.json']
    page = 'labels'

    def setUp(self):
        self.dump_data = get_content('data.json')
        self.client.force_login(user=CustomUser.objects.get(id=1))

    def test_index_page(self):
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)

        labels = Labels.objects.all()
        count = labels.count()
        self.assertEqual(count, 2)
        self.assertQuerysetEqual(
            response.context_data['labels_list'],
            labels,
            ordered=False,
        )

    def test_create(self):
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)
        new_label = self.dump_data.get('labels').get('new')
        response = self.client.post(reverse('label_create'),
                                    new_label,
                                    follow=True)
        created_label = Labels.objects.get(id=new_label.get('pk'))
        self.assertEqual(created_label.name, new_label.get('name'))
        self.assertRedirects(response, reverse('labels'))
        self.assertContains(response, _('Label successfully created!'))

    def test_update(self):
        exist_label = Labels.objects.get(id=1)
        response = self.client.get(reverse('label_update',
                                           args=[exist_label.pk]))
        self.assertEqual(response.status_code, 200)

        new_label = self.dump_data.get('labels').get('updated')
        response = self.client.post(
            reverse('label_update', args=[exist_label.pk]),
            new_label,
            follow=True
        )

        self.assertRedirects(response, reverse('labels'))
        updated_label = Labels.objects.get(pk=exist_label.pk)
        self.assertEqual(updated_label.name, new_label.get('name'))
        self.assertContains(response, _('Label successfully updated!'))

    def test_delete(self):
        exist_label = Labels.objects.get(id=2)

        response = self.client.post(reverse('label_delete',
                                            args=[exist_label.pk]),
                                    follow=True)

        self.assertRedirects(response, reverse('labels'))
        self.assertContains(response, _('Label successfully deleted!'))
        with self.assertRaises(ObjectDoesNotExist):
            Labels.objects.get(id=2)
