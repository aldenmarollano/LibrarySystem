from django.db import models

class BookCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField(max_length=500)

class Author(models.Model):
    auth_fname = models.CharField(max_length=200)
    auth_lname = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    isbn = models.CharField(null=True, blank=True, max_length=100)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='category')
    author = models.ManyToManyField(Author, related_name='author')

