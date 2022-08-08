from django.db import models
from users.models import User


class Meal(models.Model):
    employee = models.ForeignKey(
        User, related_name="meal_employees", on_delete=models.CASCADE
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    claimed = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.CharField(max_length=200)
    purpose = models.TextField()
    updated_by = models.ForeignKey(
        User, related_name="meal_updated_by", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, related_name="meal_approved_by", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"{self.employee.profile} - (XCD${self.claimed})"
