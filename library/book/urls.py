from django.urls import path
from .views import *

app_name = 'book'
urlpatterns = [
    path('book/category/register', BookCategoryRegistration.as_view(), name='create_category'),
    path('book/category/', BookCategoryList.as_view(), name='category_list'),

    path('book/register', BookRegistration.as_view(), name='register_book'),
    path('book/list', BookList.as_view(), name='book_list'),
    # path('book/list', AuthorRegistration.as_view(), name='author_register'),


    path('author/register', AuthorRegistration.as_view(), name='author_register'),
]
