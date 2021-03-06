# Generated by Django 4.0.6 on 2022-07-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_is_approver_user_is_supervisor_and_more'),
        ('overtime', '0002_alter_multiplier_options_alter_timesheet_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time_sheet_approved_by', to='users.userprofile'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='start_time',
            field=models.TimeField(default='16:30:00'),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='time_sheet_verified_by', to='users.userprofile'),
        ),
    ]
