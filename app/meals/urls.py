from django.urls import path

from . import views

app_name = "meals"

urlpatterns = [
    path("", views.MealListView.as_view(), name="meal-list"),
    path("detail/<int:pk>/", views.MealDetailView.as_view(), name="meal-detail"),
    path("update/<int:pk>/", views.MealUpdateView.as_view(), name="meal-update"),
    path("detail/<int:pk>/", views.MealDeleteView.as_view(), name="meal-delete"),
    path("create/", views.MealCreateView.as_view(), name="meal-create"),
]
