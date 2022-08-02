from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author


class AuthorsTest(APITestCase):
    def test_create_author(self):
        '''
        Проверяем возможность создать объект типа Author
        '''
        data = {
            'first_name': 'test_user',
            'last_name': 'TestLastName',
            'birthday_year': 1980,
        }  # Словарь, который будем отправлять в пост запрос
        response = self.client.post(
            '/api/authors/', data, format='json')  # Пост запрос
        # Проверяем, что запрос вернул нужный статус
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Проверяем, что количество объектов одно, а мы создали одно в рамках тестсервера
        self.assertEqual(Author.objects.count(), 1)
        # Проверяем, что имя в базе данных верное
        self.assertEqual(Author.objects.get().first_name, 'test_user')
        # Проверяем, что фамилия в базе данных верная
        self.assertEqual(Author.objects.get().last_name, 'TestLastName')
        # Проверяем, что год рождения в базе данных верный
        self.assertEqual(Author.objects.get().birthday_year, 1980)

    def test_get_author(self):
        """
        Проверяем возможность считать пользователя
        """
        data = {
            'first_name': 'test_user',
            'last_name': 'TestLastName',
            'birthday_year': 1980,
        }  # Словарь, который будем отправлять в пост запрос
        response_1 = self.client.post(
            '/api/authors/', data, format='json')  # Пост запрос
        # Снова убеждаемся, что объект создался
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        response_2 = self.client.get('/api/authors/1/')  # Гет запрос

        for key in data.keys():
            # Проверяем что по ключу key в ответе то же самое значение, что и в словаре data
            self.assertEqual(response_2.data[key], data[key])

    def test_get_authors(self):
        """
        Проверяем, что запрос на считываение пользователей возвращает код 200
        """
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
