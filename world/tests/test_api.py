import os
import django
from django.contrib.gis.geos import Point
from django.urls import reverse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geodjango.settings")
django.setup()

from django.test import TestCase, Client

from world.models import *


class WebTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username="test_username")
        self.user2 = User.objects.create(username="test_username2")
        self.guest_client = Client()
        self.memory_1 = Memory.objects.create(title='Test title 1',
                                              description='Test description 1',
                                              location=Point(0.12345678, 50.67890),
                                              user=self.user)
        self.memory_2 = Memory.objects.create(title='Test title 2',
                                              description='Test description 2',
                                              location=Point(100.12345678, 150.67890),
                                              user=self.user2)

    def test_get_index_not_login(self):
        response = self.guest_client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)

    def test_get_index_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 302)

    def test_get_list_memories_not_login(self):
        response = self.client.get(reverse('memory'))
        self.assertEqual(response.status_code, 403)

    def test_get_list_memories_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('memory'))
        self.assertEqual(response.status_code, 200)
        res = Memory.objects.filter(user_id=self.user.pk)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].title, 'Test title 1')

    def test_get_memory_login(self):
        self.client.force_login(self.user)
        url = reverse('detail_memory', args=(self.memory_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_get_memory_not_login(self):
        url = reverse('detail_memory', args=(self.memory_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_get_memory_not_owner(self):
        self.client.force_login(self.user)
        url = reverse('detail_memory', args=(self.memory_2.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

    def test_create_memory_login(self):
        self.client.force_login(self.user)
        url = reverse('new_memory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response2 = self.client.put(url, data=self.memory_1)
        self.assertEqual(response2.status_code, 200)

    def test_create_memory_not_login(self):
        url = reverse('new_memory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)