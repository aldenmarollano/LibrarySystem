# Generated by Django 5.0.7 on 2024-07-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0002_alter_borrower_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbooks',
            name='borrow_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]