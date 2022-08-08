from django import forms

from .models import TimeSheet


class TimeSheetCreateForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        fields = (
            "date",
            "reason",
            "start_time",
            "end_time",
            "multiplier",
        )
        widgets = {
            "reason": forms.Textarea(attrs={"rows": 4}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time": forms.DateInput(attrs={"type": "time"}),
            "end_time": forms.DateInput(attrs={"type": "time"}),
        }


class TimeSheetUpdateForm(forms.ModelForm):
    class Meta:
        model = TimeSheet
        fields = (
            "date",
            "reason",
            "start_time",
            "end_time",
            "multiplier",
        )
        widgets = {
            "reason": forms.Textarea(attrs={"rows": 4}),
            "date": forms.DateInput(attrs={"type": "date"}),
        }
