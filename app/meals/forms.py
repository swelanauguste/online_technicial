from django import forms

from .models import Meal


class MealCreateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ("purpose", "location", "start_time", "end_time", "claimed")
        widgets = {
            "purpose": forms.Textarea(attrs={"rows": 4}),
            "start_time": forms.DateInput(attrs={"type": "time"}),
            "end_time": forms.DateInput(attrs={"type": "time"}),
            "claimed": forms.TextInput(attrs={"placeholder": "$25.00"}),
        }


class MealUpdateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ("purpose", "location", "start_time", "end_time", "claimed")
        widgets = {
            "purpose": forms.Textarea(attrs={"rows": 4}),
            "claimed": forms.TextInput(attrs={"placeholder": "$25.00"}),
        }
