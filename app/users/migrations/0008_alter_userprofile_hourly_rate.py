# Generated by Django 4.1 on 2022-08-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_userprofile_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="hourly_rate",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=9, null=True
            ),
        ),
    ]
