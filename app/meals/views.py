from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import MealCreateForm, MealUpdateForm
from .models import Meal


class MealListView(ListView):
    model = Meal


class MealDetailView(DetailView):
    model = Meal


class MealUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Meal
    form_class = MealUpdateForm
    success_message = "Your meal was updated successfully"
    success_url = reverse_lazy("meals:meal-list")

    def test_func(self):
        if self.request.user == self.get_object().employee:
            return True
        return False

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class MealCreateView(SuccessMessageMixin, CreateView):
    model = Meal
    form_class = MealCreateForm
    success_message = "Your meal was added successfully"
    success_url = reverse_lazy("meals:meal-list")

    def form_valid(self, form):
        form.instance.employee = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class MealDeleteView(SuccessMessageMixin, DeleteView):
    model = Meal
    success_message = "Your meal was deleted"
    success_url = reverse_lazy("meals:meal-list")

    def test_func(self):
        if self.request.user == self.get_object().created_by:
            return True
        return False
