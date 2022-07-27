from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("userprofiles/", views.UserProfileListView.as_view(), name="user-profile-list"),
    path("user/<int:pk>/", views.UserUpdateView.as_view(), name="user-update"),
    path(
        "user-profile/<slug:slug>/<int:pk>/",
        views.UserProfileUpdateView.as_view(),
        name="user-profile-update",
    ),
]
