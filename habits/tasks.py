from datetime import datetime, timedelta
import time
from celery import shared_task

from habits.models import Habit
from services.telegram_intergation import TelegramBotService


@shared_task
def send_reminder_beginning_week():
    # привычки ежедневные
    habits_everyday = Habit.objects.filter(sign_pleasant_habit=False, frequency="7")

    # привычки еженедельные (реже одного раза в день)
    habits_other = Habit.objects.filter(sign_pleasant_habit=False)

    # текущий день недели
    day_week_now = datetime.now().weekday()

    # текущее время
    time_now = time.strftime("%H:%M", time.localtime())

    if day_week_now == 0:
        text = f'На этой неделе необходимо выполнить:\n'
        for habit in habits_other:
            text += f'{habit.action}, на {habit.place}'
            message = TelegramBotService(chat_id=habit.chat_id, text=text)
            message.send_message_tg()

    for habit in habits_everyday:
        text = (f'В {habit.time} необходимо выполнить:\n'
                f'{habit.action} в течении {habit.time_to_complete} секунд!\n')
        if time_now > (habit.time - timedelta(minutes=30)):
            message = TelegramBotService(chat_id=habit.chat_id, text=text)
            message.send_message_tg()
