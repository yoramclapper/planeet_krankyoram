from django.shortcuts import redirect
from django.views.generic import TemplateView


class BudgetView(TemplateView):
    template_name = "financien/budget.html"
