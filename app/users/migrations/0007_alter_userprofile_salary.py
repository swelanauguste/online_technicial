# Generated by Django 4.0.6 on 2022-08-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_userprofile_hourly_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='salary',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]
