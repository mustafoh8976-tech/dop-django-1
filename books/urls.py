from django.urls import path

from .views import create_books, delete_books, list_books, update_books

urlpatterns = [
    path('', list_books, name='list_books'),
    path('create/', create_books, name='create_books'),
    path('delete/<int:pk>/', delete_books, name='delete_books'),
    path('update/<int:pk>/', update_books, name='update_books'),
]
