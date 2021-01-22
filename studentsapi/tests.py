import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.test import APITestCase


class StudentApiTests(APITestCase):
    User = get_user_model()

    def setUp(self):
        self.USERNAME = 'tester'
        self.EMAIL = 'tester@example.com'
        self.PASSWORD = 'password'
        self.user = self.User.objects.create_user(
            self.USERNAME, self.EMAIL, self.PASSWORD)

    def tearDown(self):
        self.client.logout()

    def test_of_view(self):
        income_data = {
            'fio': 'tester',
            'record_status': '5',
        }
        response = self.client.post(reverse('info-list'), income_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_authenticate(self.user)

        response = self.client.post(reverse('info-list'), income_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(reverse('info-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(force_str(response.content))
        self.assertEqual(data[0]['fio'], income_data['fio'])

        kwargs = {'pk': data[0]['id']}
        response = self.client.put(reverse('info-detail', kwargs=kwargs),
                                   income_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(reverse('info-detail', kwargs=kwargs))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
