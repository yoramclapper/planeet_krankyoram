from django.urls import path
from .views import BudgetView, create_sheet

urlpatterns = [
    path("financien/", BudgetView.as_view(), name="budget"),
    path("financien/sheet_form/", create_sheet, name="sheet_form")
]
