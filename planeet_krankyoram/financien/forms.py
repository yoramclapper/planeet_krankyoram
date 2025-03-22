from django.forms import ModelForm
from .models import BudgetSheet


class BudgetSheetForm(ModelForm):
    class Meta:
        model = BudgetSheet
        fields = ["sheet_name", "start_date"]
