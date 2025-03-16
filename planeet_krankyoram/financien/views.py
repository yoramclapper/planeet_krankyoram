from django.shortcuts import redirect
from django.views.generic import ListView
from core.models import AppsLib


class BudgetView(ListView):
    context_object_name = "my_apps"
    queryset = AppsLib.objects.filter(show=True)
    template_name = "financien/budget.html"
