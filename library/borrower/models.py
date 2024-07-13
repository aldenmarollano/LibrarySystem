from django.db import models
from book.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

class Borrower(models.Model):
    id_num = models.CharField(max_length=1000)
    stud_fname = models.CharField(max_length=200)
    stud_lname = models.CharField(max_length=200)
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class BorrowedBooks(models.Model):
    borrower = models.ForeignKey(Borrower, related_name='borrower', on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    borrow_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField()

