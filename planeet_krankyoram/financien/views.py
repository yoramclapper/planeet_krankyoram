from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, UpdateView
from .forms import BudgetSheetForm, BudgetActualForm
from .models import BudgetSheet, Budget, BudgetActual, BudgetCategory


class BudgetView(TemplateView):
    template_name = "financien/budget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'pk' not in self.kwargs:
            sheet = BudgetSheet.objects.latest("start_date")
        else:
            sheet = BudgetSheet.objects.get(pk=self.kwargs.get("pk"))
        context['categories'] = BudgetCategory.objects.all()
        context['sheet'] = sheet
        context['actuals'] = BudgetActual.objects.filter(sheet_id=sheet.id)
        return context


class CreateSheetView(FormView):
    form_class = BudgetSheetForm
    template_name = "financien/form.html"
    success_url = "/financien/"

    def form_valid(self, form):
        sheet = BudgetSheet(
            sheet_name=form.cleaned_data['sheet_name'],
            start_date=form.cleaned_data['start_date']
        )
        sheet.save()
        sheet.create_actuals()
        return super().form_valid(form)


class ArchiveView(ListView):
    template_name = 'financien/archive.html'
    model = BudgetSheet
    context_object_name = "budget_sheets"
    ordering = '-start_date'


class ActualUpdateView(UpdateView):
    form_class = BudgetActualForm
    template_name = "financien/form.html"
    model = BudgetActual
    success_url = "/financien/"


