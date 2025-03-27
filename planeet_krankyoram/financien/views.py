from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import BudgetSheetForm
from .models import BudgetSheet, Budget, BudgetActual


class BudgetView(TemplateView):
    template_name = "financien/budget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sheet = BudgetSheet.objects.latest("start_date")
        context['sheet'] = sheet
        context['actuals'] = BudgetActual.objects.filter(sheet_id=sheet.id)
        return context


class CreateSheetView(FormView):
    form_class = BudgetSheetForm
    template_name = "financien/add_sheet.html"
    success_url = "/financien/"

    def form_valid(self, form):
        sheet = BudgetSheet(
            sheet_name=form.cleaned_data['sheet_name'],
            start_date=form.cleaned_data['start_date']
        )
        sheet.save()
        sheet.create_actuals()
        return super().form_valid(form)


def sheet_form_handler(request):
    if request.method == "POST":
        form = BudgetSheetForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/financien/")
    else:
        form = BudgetSheetForm()
    return render(request, "financien/add_sheet.html", {"form": form})

