# Generated by Django 5.0.7 on 2024-07-12 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_num', models.CharField(max_length=1000)),
                ('stud_fname', models.CharField(max_length=200)),
                ('stud_lname', models.CharField(max_length=200)),
                ('year', models.IntegerField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now=True)),
                ('return_date', models.DateTimeField()),
                ('book', models.ManyToManyField(to='book.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to='borrower.borrower')),
            ],
        ),
    ]
