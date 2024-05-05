from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import HabitsListPaginations
from habits.permissions import IsOwnerHabit
from habits.serializers import HabitSerializer, HabitPublicSerializer


# Create your views here.
class HabitCreateAPIView(CreateAPIView):
    """ Контроллер создания экземпляра привычки """

    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """ Автоматическое сохраниение пользователя во владельцы создаваемой привычки"""
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class HabitListAPIView(ListAPIView):
    """ Контроллер просмотра списка привычек"""
    serializer_class = HabitSerializer
    # permission_classes = [IsOwnerHabit]
    permission_classes = [AllowAny]
    pagination_class = HabitsListPaginations

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """ Контроллер просмотра экземпляра привычек"""
    serializer_class = HabitSerializer
    # permission_classes = [IsOwnerHabit]
    permission_classes = [AllowAny]
    queryset = Habit.objects.all()


class HabitUpdateAPIView(UpdateAPIView):
    """ Контроллер обновления привычки"""
    serializer_class = HabitSerializer
    # permission_classes = [IsOwnerHabit]
    permission_classes = [AllowAny]
    queryset = Habit.objects.all()


class HabitDestroyAPIView(DestroyAPIView):
    """ Контроллер удаления привычки"""
    serializer_class = HabitSerializer
    # permission_classes = [IsOwnerHabit]
    permission_classes = [AllowAny]


class HabitsPublicListAPIView(ListAPIView):
    """ Контроллер просмотра списка публичных привычек"""
    serializer_class = HabitPublicSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = HabitsListPaginations
    queryset = Habit.objects.filter(is_publicity=True)
