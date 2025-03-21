from django.db import models
from django.core.validators import MinValueValidator
import datetime


class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Budget categories'

    def __str__(self):
        return self.category_name


class Budget(models.Model):
    budget_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(BudgetCategory, models.SET_NULL, blank=True, null=True)
    budget = models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Budget (in centen)")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.budget_name


class BudgetSheet(models.Model):
    sheet_name = models.CharField(max_length=255)
    start_date = models.DateField(unique=True, default=datetime.datetime.now().date())

    def __str__(self):
        return self.sheet_name


class BudgetActual(models.Model):
    sheet = models.ForeignKey(BudgetSheet, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    actual = models.IntegerField(validators=[MinValueValidator(0)])
