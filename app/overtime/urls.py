from django.urls import path

from . import views

app_name = "overtime"

urlpatterns = [
    path("", views.TimeSheetListView.as_view(), name="time-sheet-list"),
    path("create/", views.TimeSheetCreateView.as_view(), name="time-sheet-create"),
    path(
        "pending-approval/",
        views.TimeSheetPendingApprovalListView.as_view(),
        name="time-sheet-pending-approval",
    ),
    # path(
    #     "filter-list/",
    #     views.TimeSheetFilterListView.as_view(),
    #     name="time-sheet-filter-list",
    # ),
    path(
        "update/<int:pk>/",
        views.TimeSheetUpdateView.as_view(),
        name="time-sheet-update",
    ),
    path(
        "delete/<int:pk>/",
        views.TimeSheetDeleteView.as_view(),
        name="time-sheet-delete",
    ),
]
