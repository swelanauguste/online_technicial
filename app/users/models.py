import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# from django.urls import reverse


class User(AbstractUser):
    is_supervisor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse("users:user-update", kwargs={"pk": self.pk})


class JobTitle(models.Model):
    job_title = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.job_title


class Department(models.Model):
    department = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.department


class UserProfile(models.Model):
    GENDER_LIST = [
        ("M", "M"),
        ("F", "F"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=65, blank=True)
    employee_id = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=65, blank=True)
    last_name = models.CharField(max_length=65, blank=True)
    job_title = models.ForeignKey(JobTitle, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    salary = models.PositiveSmallIntegerField(default=0)
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_LIST)
    dob = models.DateField("DOB", blank=True, null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=25, blank=True, default="50")
    hourly_rate = models.DecimalField(decimal_places=2, max_digits=9, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        if not self.hourly_rate:
            self.hourly_rate = (((self.salary * 12) / 52) / 5) / 8
        super(UserProfile, self).save(*args, **kwargs)

    @property
    def get_employee_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("users:user-profile-update", kwargs={"pk": self.pk, "slug": self.slug})

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.username
