from django.db import models

from users.models import User
from services.constants import *


class Habit(models.Model):
    """
    Модель привычки
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits', verbose_name='владелец')
    place = models.CharField(max_length=15, choices=PLACE, verbose_name='место выполнения')
    time = models.DateTimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=150, verbose_name='действие')
    sign_pleasant_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey(to='Habit', verbose_name='cвязанная привычка')
    frequency = models.CharField(max_length=10, choices=FREQUENCY, default='7', verbose_name='периодичность выполенения')
    award = models.CharField(max_length=100, verbose_name='награда')
    time_to_complete = models.IntegerField(verbose_name='время на выполнение')
    is_publicity = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        """
        строковое отображение модели
        """
        return f'{self.owner}: {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'