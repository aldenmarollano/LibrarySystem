from django import forms
from .models import Book, BookCategory, Author


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['category_name', 'category_description']


class AuthorForm(forms.ModelForm):
    auth_fname = forms.CharField(label='First Name')
    auth_lname = forms.CharField(label='Last Name')
    class Meta:
        model = Author
        fields = ['auth_fname', 'auth_lname']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn', 'category', 'author']