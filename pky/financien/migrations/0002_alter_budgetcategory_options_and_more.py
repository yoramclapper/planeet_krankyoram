# Generated by Django 4.2.20 on 2025-03-21 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financien', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budgetcategory',
            options={'verbose_name_plural': 'Budget categories'},
        ),
        migrations.RemoveField(
            model_name='budgetsheet',
            name='startdate',
        ),
        migrations.AddField(
            model_name='budget',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='budgetsheet',
            name='start_date',
            field=models.DateField(default=datetime.date(2025, 3, 21), unique=True),
        ),
    ]
