# Generated by Django 5.0.7 on 2024-07-13 00:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
