from django.contrib import admin

from .models import Department, JobTitle, User, UserProfile

admin.site.register(Department)
admin.site.register(JobTitle)
admin.site.register(User)
admin.site.register(UserProfile)
