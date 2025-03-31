from django.contrib import admin
from .models import BudgetCategory, Budget, BudgetSheet

admin.site.register(BudgetCategory)
admin.site.register(Budget)
admin.site.register(BudgetSheet)
