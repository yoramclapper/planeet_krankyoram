from django.urls import path
from .views import BudgetView, CreateSheetView, ArchiveView

urlpatterns = [
    path("financien/", BudgetView.as_view(), name="budget"),
    path("financien/add_sheet/", CreateSheetView.as_view(), name="add_sheet"),
    path("financien/archive/", ArchiveView.as_view(), name="archive"),
]
