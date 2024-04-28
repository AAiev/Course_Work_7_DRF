from rest_framework.serializers import ValidationError

from services.constants import TIME_COMPLATE

class HabitValidator:
    """
    валидацция невозможности одновременного заполнения связанной привычки и вознаграждения
    """
    def __init__(self, related_habit, award):
        self.related_habit = related_habit
        self.award = award

    def __call__(self, value):
        related_habit = value.get('related_habit')
        award = value.get('award')
        if related_habit and award:
            raise ValidationError("Запрещено выбирать односременно связанную привычку и вознаграждение")



class TimeCompleteValidator:
    """
    Валидация времени выполнения привычки. не более TIME_COMPLATE секунд.
    TIME_COMPLATE - время указывается в файле services/constants.py
    """

    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        time_to_complete = value.get('time_to_complete')
        if time_to_complete > TIME_COMPLATE:
            raise ValidationError(f"Время выполнения привычки должно быть не больше {TIME_COMPLATE} секунд)")
