from django.forms import ModelForm
from django import forms
from .models import BudgetSheet, BudgetActual
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.urls import reverse


class BudgetSheetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Opslaan'))
        self.helper.add_input(Button('cancel', 'Annuleer', css_class='btn-secondary', onclick="window.location.href = '{}';".format(reverse('budget'))))

    class Meta:
        model = BudgetSheet
        fields = ["sheet_name", "start_date"]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }


class BudgetActualForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Opslaan'))
        self.helper.add_input(Button('cancel', 'Annuleer', css_class='btn-secondary', onclick="window.location.href = '{}';".format(reverse('budget'))))

    class Meta:
        model = BudgetActual
        fields = ["actual"]
