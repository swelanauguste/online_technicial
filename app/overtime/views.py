from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView
from users.models import UserProfile

from .forms import TimeSheetCreateForm
from .models import TimeSheet


class TimeSheetListView(ListView):
    model = TimeSheet
    # template_name = "overtime/timesheet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = TimeSheet.objects.filter(
            created_by=self.request.user.profile
        )
        context["employee_list"] = UserProfile.objects.all()
        return context


class TimeSheetFilterListView(ListView):
    model = TimeSheet
    template_name = "overtime/timesheet_filter_list.html"

    def get_queryset(self):
        queryset = TimeSheet.objects.all()
        employee = self.request.GET.get("employee")
        start_date = self.request.GET.get("start_date")
        end_date = self.request.GET.get("end_date")
        print(start_date, "start_date", end_date, "end_date")
        if start_date:
            queryset = queryset.filter(
                Q(id=employee) | Q(date__gte=start_date) | Q(date__lte=end_date)
            ).distinct()
            print(queryset, "queryset")
        return queryset


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

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        form.instance.updated_by = self.request.user.profile
        return super().form_valid(form)
