from django import forms
from .models import *


class TaskForm(forms.Form):
    class Meta:
        model = Task
        fields = ["name", "due_date", "taskgroup"]
        widgets = {
            'due_date': forms.TextInput(
                attrs={'type': 'datetime=local'}
            )
        }
