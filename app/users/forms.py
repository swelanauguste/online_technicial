from django import forms

from .models import User, UserProfile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("is_supervisor", "is_admin")


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "gender", "dob", "bio", "phone")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
            "dob": forms.DateInput(attrs={"type": "date"}),
        }
