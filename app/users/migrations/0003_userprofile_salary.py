# Generated by Django 4.0.6 on 2022-07-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='salary',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
