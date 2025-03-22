from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import BudgetSheetForm


class BudgetView(TemplateView):
    template_name = "financien/budget.html"


def create_sheet(request):
    if request.method == "POST":
        form = BudgetSheetForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/financien/")
    else:
        form = BudgetSheetForm()
    return render(request, "financien/create_sheet.html", {"form": form})

