from django.contrib import admin
from .models import BorrowedBooks, Borrower

admin.site.register(BorrowedBooks)
admin.site.register(Borrower)
