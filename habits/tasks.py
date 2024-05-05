import datetime
from celery import shared_task

from habits.models import Habit
from services.telegram_intergation import TelegramBotService


# текущия дата и время
now = datetime.datetime.today()

# текущий день недели
day_week_now = now.weekday()

# текущее время
time_now = datetime.datetime.now().time().strftime('%H:%M')


@shared_task
def send_reminder_habit_everyday():
    # привычки ежедневные
    habits_everyday = Habit.objects.filter(sign_pleasant_habit=False) & Habit.objects.filter(frequency='7')

    for habit in habits_everyday:
        if habit.time.strftime('%H:%M') == time_now:
            text = (f'В {habit.time.strftime("%H:%M")} необходимо выполнить:\n'
                    f'{habit.action} в течении {habit.time_to_complete} секунд!\n')
            message = TelegramBotService(chat_id=habit.owner.chat_id, text=text)
            message.send_message_tg()


@shared_task
def send_reminder_habit_everyweek():
    # привычки еженедельные (реже одного раза в день)
    habits_other = Habit.objects.exclude(sign_pleasant_habit=True) & Habit.objects.exclude(frequency='7')

    time_1 = datetime.time(8, 00)
    time_from = time_1.strftime('%H:%M')
    time_2 = datetime.time(8, 30)
    time_to = time_2.strftime('%H:%M')

    if day_week_now == 0:
        if time_now >= time_from:
            if time_now < time_to:
                text_ = f'На этой неделе необходимо выполнить:\n'
                for habit in habits_other:
                    text = text_ + f'{habit.action} на {habit.place}\n'
                    message = TelegramBotService(chat_id=habit.owner.chat_id, text=text)
                    message.send_message_tg()
