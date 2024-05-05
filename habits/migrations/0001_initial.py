# Generated by Django 5.0.4 on 2024-04-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(choices=[('HOME', 'дома'), ('STUDY', 'на учебе'), ('WORK', 'на работе'), ('STREET', 'на улице'), ('OTHER', 'в другом месте')], max_length=15, verbose_name='место выполнения')),
                ('time', models.DateTimeField(verbose_name='время выполнения')),
                ('action', models.CharField(max_length=150, verbose_name='действие')),
                ('sign_pleasant_habit', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('frequency', models.CharField(choices=[('1', '1 раз в неделю'), ('2', '2 раз в неделю'), ('3', '3 раз в неделю'), ('4', '4 раз в неделю'), ('5', '5 раз в неделю'), ('6', '6 раз в неделю'), ('7', 'каждый день')], default='7', max_length=10, verbose_name='периодичность выполенения')),
                ('award', models.CharField(blank=True, max_length=100, null=True, verbose_name='награда')),
                ('time_to_complete', models.IntegerField(verbose_name='время на выполнение')),
                ('is_publicity', models.BooleanField(default=False, verbose_name='признак публичности')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]