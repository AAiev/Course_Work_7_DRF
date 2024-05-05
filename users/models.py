from django.contrib.auth.models import AbstractUser
from django.db import models

from services.constants import NULLABLE


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активность')
    chat_id = models.CharField(max_length=100, verbose_name='id чата в ТГ', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f' {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
