from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UsersTest(APITestCase):
    def test_create_user(self):
        '''
        Ensure we can create a new author object.
        '''
        data = {
            'username': 'test_user',
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'email': 'testusermail@localhost',
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test_user')
        self.assertEqual(User.objects.get().first_name, 'TestFirstName')
        self.assertEqual(User.objects.get().last_name, 'TestLastName')
        self.assertEqual(User.objects.get().email, 'testusermail@localhost')

    def test_get_user(self):
        data = {
            'username': 'test_user',
            'first_name': 'TestFirstName',
            'last_name': 'TestLastName',
            'email': 'testusermail@localhost',
        }
        response_1 = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        response_2 = self.client.get('/api/users/1/')

        for key in data.keys():
            self.assertEqual(response_2.data[key], data[key])

    def test_get_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
