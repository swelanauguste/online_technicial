from datetime import datetime, time

from django.db import models
from django.urls import reverse
from users.models import User, UserProfile


class Multiplier(models.Model):
    multiplier = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("multiplier",)

    def __str__(self):
        return f"{self.multiplier}"


class TimeSheet(models.Model):
    employee = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.DateField()
    reason = models.TextField("reason for overtime")
    start_time = models.TimeField(default="16:30:00")
    end_time = models.TimeField(default="18:30:00")
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="time_sheet_approved_by",
        blank=True
    )
    multiplier = models.ForeignKey(Multiplier, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="time_sheet_verified_by",
        blank=True
    )
    created_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="time_sheet_created_by",
    )

    updated_by = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name="time_sheet_updated_by",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        ordering = ("-created_at",)

    # def get_absolute_url(self):
    #     return reverse("overtime:overtime-detail", kwargs={"pk": self.pk})

    @property
    def time_diff(self):
        return (
            datetime.strptime(str(self.end_time), "%H:%M:%S")
            - datetime.strptime(str(self.start_time), "%H:%M:%S")
        ).seconds / 3600

    @property
    def get_overtime(self):
        overtime = (float(self.multiplier.multiplier) * float(self.time_diff)) * float(
            self.employee.hourly_rate
        )
        return f"{overtime:.2f}"

    def __str__(self):
        return f"${self.get_overtime} ({self.time_diff} hours)"
