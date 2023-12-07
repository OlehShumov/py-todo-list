from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control"}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tag": forms.CheckboxSelectMultiple,
        }
