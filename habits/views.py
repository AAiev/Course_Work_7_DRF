контроллеры from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsOwnerHabit
from habits.serializers import HabitSerializer


# Create your views here.
class HabitCreateAPIView(CreateAPIView):
    """ Контроллер создания экземпляра привычки """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """ Автоматическое сохраниение пользователя во владельцы создаваемой привычки"""
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        new_habit.save()


class HabitListAPIView(ListAPIView):
    """ Контроллер просмотра списка привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerHabit]
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Контроллер просмотра экземпляра привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerHabit]
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """ Контроллер обновления привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerHabit]
    queryset = Habit.objects.all()


class HabitDestroyAPIView(DestroyAPIView):
    """ Контроллер удаления привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerHabit]
