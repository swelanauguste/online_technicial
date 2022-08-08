from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls", namespace="users")),
    path("overtime/", include("overtime.urls", namespace="overtime")),
    path("meals/", include("meals.urls", namespace="meals")),
]
