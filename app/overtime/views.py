from datetime import datetime

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.models import UserProfile

from .forms import TimeSheetCreateForm, TimeSheetUpdateForm
from .models import TimeSheet


class TimeSheetListView(ListView):
    model = TimeSheet
    template_name = "overtime/timesheet_list.html"
    paginate_by = 30

    def get_context_data(self, *args, **kwargs):
        context = super(TimeSheetListView, self).get_context_data(*args, **kwargs)
        context["employee_list"] = UserProfile.objects.all()
        return context

    def get_queryset(self):
        queryset = TimeSheet.objects.filter(created_by=self.request.user).order_by(
            "date", "start_time"
        )
        employee = self.request.GET.get("employee")
        start_date = self.request.GET.get("start_date")
        # start_date = datetime.strptime(start_date_a, '%Y-%m-%d').date()
        end_date = self.request.GET.get("end_date")
        # end_date = datetime.strptime(end_date_a, '%Y-%m-%d').date()
        if start_date != "" and start_date is not None:
            if end_date != "" and end_date is not None:
                if employee != "" and employee is not None:
                    queryset = queryset.filter(
                        Q(id=employee)
                        | Q(
                            date__gte=datetime.strptime(start_date, "%Y-%m-%d").date(),
                            date__lte=datetime.strptime(end_date, "%Y-%m-%d").date(),
                        )
                    ).distinct()
        return queryset


# class TimeSheetFilterListView(ListView):
#     model = TimeSheet
#     template_name = "overtime/timesheet_filter_list.html"

#     def get_queryset(self):
#         queryset = TimeSheet.objects.all()
#         employee = self.request.GET.get("employee")
#         start_date = self.request.GET.get("start_date")
#         end_date = self.request.GET.get("end_date")
#         print(start_date, "start_date", end_date, "end_date")
#         if start_date or end_date or employee:
#             queryset = queryset.filter(
#                 Q(id=employee) | Q(date__range=[start_date, end_date])
#             ).distinct()
#             print(queryset, "queryset")
#         return queryset


class TimeSheetPendingApprovalListView(ListView):
    model = TimeSheet
    template_name = "overtime/timesheet_pending_approval_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = TimeSheet.objects.filter(is_approved=False)
        # print('context', context["time_sheet_pending_approval"])
        return context


class TimeSheetCreateView(SuccessMessageMixin, CreateView):
    model = TimeSheet
    form_class = TimeSheetCreateForm
    success_message = "Your time sheet was added successfully"
    success_url = reverse_lazy("overtime:time-sheet-list")

    def form_valid(self, form):
        form.instance.employee = self.request.user
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TimeSheetUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = TimeSheet
    form_class = TimeSheetUpdateForm
    success_message = "Your time sheet was updated successfully"
    success_url = reverse_lazy("overtime:time-sheet-list")

    def test_func(self):
        if self.request.user == self.get_object().created_by:
            return True
        return False

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class TimeSheetDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = TimeSheet
    success_message = "Your time sheet was deleted"
    success_url = reverse_lazy("overtime:time-sheet-list")

    def test_func(self):
        if self.request.user == self.get_object().created_by:
            return True
        return False

