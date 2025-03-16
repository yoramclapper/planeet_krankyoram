from django.urls import path
from .views import BudgetView

urlpatterns = [
    path("financien/", BudgetView.as_view(), name="budget"),
]
