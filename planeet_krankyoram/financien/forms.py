from django.forms import ModelForm
from django import forms
from .models import BudgetSheet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BudgetSheetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Save'))

    class Meta:
        model = BudgetSheet
        fields = ["sheet_name", "start_date"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }
