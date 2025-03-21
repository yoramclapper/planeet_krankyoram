from django.db import models
from django.core.validators import MinValueValidator


class BudgetCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True)


class Budget(models.Model):
    budget_name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(BudgetCategory, models.SET_NULL, blank=True, null=True)
    budget = models.IntegerField(validators=[MinValueValidator(0)])
    isactive = models.BooleanField


class BudgetSheet(models.Model):
    sheet_name = models.CharField(max_length=255)
    startdate = models.DateField(unique=True)


class BudgetActual(models.Model):
    sheet = models.ForeignKey(BudgetSheet, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    actual = models.IntegerField(validators=[MinValueValidator(0)])
