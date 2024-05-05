from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.test',
            password='123'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place='HOME',
            time='12:00',
            action='действие',
            award='награда',
            time_to_complete=120,
            is_publicity=True
        )

        self.response_verification = {
            'id': self.habit.pk, 'owner': self.user.pk,
            'place': 'HOME', 'time': '12:00:00',
            'action': 'действие', 'sign_pleasant_habit': False,
            'related_habit': None, 'frequency': '7',
            'award': 'награда', 'time_to_complete': 120,
            'is_publicity': True}

    def test_habit_create(self):
        """ Тестирование создания сущности модели Habit"""
        data = {
            "owner": self.user.pk,
            "place": "HOME",
            "time": "15:20",
            "action": "Приседания",
            "award": "sweet",
            "time_to_complete": 120
        }
        response = self.client.post(
            reverse('habits:habit-create'),
            data=data
        )

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)

        response.json().pop('id')
        response.json().pop('owner')
        response_verification = {
            'place': 'HOME', 'time': '15:20:00',
            'action': 'Приседания', 'sign_pleasant_habit': False,
            'related_habit': None, 'frequency': '7',
            'award': 'sweet', 'time_to_complete': 120,
            'is_publicity': False}

        self.assertEqual(response.json(),
                         response_verification)

    def test_habit_detail(self):
        """ Тестирование отображения экземпляра сущности модели Habit"""

        response = self.client.get(
            reverse('habits:habit-detail', args=[self.habit.pk])
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         self.response_verification)

    def test_habit_list(self):
        """ Тестирование отображения списка сущностей модели Habit"""

        response = self.client.get(
            reverse('habits:habit-list')
        )

        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        self.assertEqual(response.json(),
                         {'count': 1, 'next': None, 'previous': None,
                           'results': [self.response_verification]})
