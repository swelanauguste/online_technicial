from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, UpdateView

from .forms import UserProfileUpdateForm, UserUpdateForm
from .models import User, UserProfile


class IndexView(TemplateView):
    template_name = "index.html"


class UserListView(ListView):
    model = User


class UserProfileListView(ListView):
    model = UserProfile


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm


class UserProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileUpdateForm
    success_message = "Your profile was updated successfully"
