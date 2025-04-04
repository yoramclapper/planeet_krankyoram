# Generated by Django 4.2.20 on 2025-03-31 19:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financien', '0002_alter_budgetcategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetcategory',
            name='display_order',
            field=models.IntegerField(default=9999, unique=True, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='budget',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Budget'),
        ),
        migrations.AlterField(
            model_name='budgetactual',
            name='actual',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Werkelijk bedrag'),
        ),
        migrations.AlterField(
            model_name='budgetsheet',
            name='sheet_name',
            field=models.CharField(max_length=255, verbose_name='Naam blad'),
        ),
        migrations.AlterField(
            model_name='budgetsheet',
            name='start_date',
            field=models.DateField(unique=True, verbose_name='Start datum'),
        ),
    ]
