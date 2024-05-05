from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateAPIView, HabitListAPIView,
                          HabitRetrieveAPIView, HabitUpdateAPIView,
                          HabitDestroyAPIView, HabitsPublicListAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('', HabitListAPIView.as_view(), name='habit-list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit-delete'),
    path('public/', HabitsPublicListAPIView.as_view(), name='habit-public'),

]
