from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .forms import *
from .models import *

class BookCategoryRegistration(View):
    def get(self, request):
        form = BookCategoryForm()
        context = {
            'form':form
        }
        return render(request, 'book/category/category_registration.html', context)
    
    def post(self, request):
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Saved')
        return redirect('book:category_list')
    
class BookCategoryList(View):
    def get(self, request):
        queryset = BookCategory.objects.all()
        context = {
            'category_list':queryset
        }
        return render(request, 'book/category/category_list.html', context)

class BookRegistration(View):
    def get(self, request):
        form = BookForm()
        context = {
            'form':form
        }
        return render(request, 'book/book_registration.html', context)
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Book Saved')




class AuthorRegistration(View):
    def get(self, request):
        form = AuthorForm()
        context = {
            'form':form
        }
        return render(request, 'author/author_registration.html', context)
    
    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Author Saved')

