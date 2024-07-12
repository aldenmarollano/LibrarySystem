from django.db import models
from book.models import Book

class Borrower(models.Model):
    id_num = models.CharField(max_length=1000)
    stud_fname = models.CharField(max_length=200)
    stud_lname = models.CharField(max_length=200)
    year = models.IntegerField(max_length=1)

class BorrowedBooks(models.Model):
    borrower = models.ForeignKey(Borrower, related_name='borrower', on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)
    borrow_date = models.DateTimeField(auto_now=True)
    return_date = models.DateTimeField()

