from rest_framework.serializers import ValidationError


class HabitValidator:
    """
    валидацция невозможности одновременного заполнения связанной привычки и вознаграждения
    """
    def __init__(self, related_habit, award):
        self.related_habit = related_habit
        self.award = award

    def __call__(self, value):
        if self.related_habit and self.award:
            raise ValidationError("Запрещено выбирать односременно связанную привычку и вознаграждение")

