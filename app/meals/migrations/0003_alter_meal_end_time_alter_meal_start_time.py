# Generated by Django 4.0.6 on 2022-08-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_rename_mealallowance_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='end_time',
            field=models.TimeField(default='7:00'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='start_time',
            field=models.TimeField(default='4:30'),
        ),
    ]
