from rest_framework import serializers
from habits.models import Habit

from habits.validators import (HabitValidator, TimeCompleteValidator,
                               SignPleasantHabitAndRelatedHabitValidator, PleasantHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Привычек
    """
    class Meta:
        model = Habit
        fields = ('id', 'owner', 'place', 'time', 'action', 'sign_pleasant_habit', 'related_habit',
                  'frequency', 'award', 'time_to_complete', 'is_publicity',)
        validators = [
            HabitValidator(related_habit='related_habit',
                           award='award'),
            TimeCompleteValidator(time_to_complete='time_to_complete'),

            SignPleasantHabitAndRelatedHabitValidator(related_habit='related_habit'),

            PleasantHabitValidator(sign_pleasant_habit='sign_pleasant_habit',
                                   related_habit='related_habit',
                                   award='award')
        ]
