from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User


class UsersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.test',
            password='123',
            chat_id='123456789a'
        )

    def test_user_create(self):
        """ Тест создания пользователя """

        data = {
            "email": "test111@test.test",
            "password": "12345678",
            "chat_id": "test111"
        }
        response = self.client.post(
            reverse('users:user-create'),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED
                         )

        response.json().pop('id')
        response.json().pop('password')

        self.assertEqual(
            response.json(),
            {
                'email': 'test111@test.test',
                'chat_id': 'test111'
            }
        )

    def test_user_retrieve(self):
        """ Тест отображения экзмепляра пользователя """

        response = self.client.get(
            reverse('users:user-detail', args=[self.user.pk])
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )

        self.assertEqual(
            response.json(),
            {'id': self.user.pk, 'email': 'test@test.test', 'chat_id': '123456789a', 'password': '123'}
        )

    def test_user_list(self):
        """ Тест отображения списка пользователей """

        response = self.client.get(
            reverse('users:user-list')
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )
        response_without_id = []
        for i in response.data:
            i.pop('id')
            response_without_id.append(i)

        self.assertEqual(
            response_without_id,
            [{'email': 'test@test.test', 'chat_id': '123456789a', 'password': '123'}]
        )

    def test_user_update(self):
        """ Тест обновления экземпляра пользователя """

        data = {
            'chat_id': '111111test'
        }
        response = self.client.patch(
            reverse('users:user-update', args=[self.user.pk]),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK
                         )

        self.assertEqual(
            response.json(),
            {'id': self.user.pk, 'email': 'test@test.test', 'chat_id': '111111test', 'password': '123'}
        )

    def test_user_delete(self):
        """ Тест удаления пользователя """

        response = self.client.delete(
            reverse('users:user-delete', args=[self.user.pk])
        )

        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT
                         )
