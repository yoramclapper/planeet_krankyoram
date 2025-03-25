from django.forms import ModelForm
from django import forms
from .models import BudgetSheet


class BudgetSheetForm(ModelForm):
    class Meta:
        model = BudgetSheet
        fields = ["sheet_name", "start_date"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
