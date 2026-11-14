from django.shortcuts import redirect, render

from .models import Books


def list_books(request):
    books = Books.objects.all()
    return render(request, 'list_book.html', {'books': books})


def create_books(request):
    if request.method == 'POST':
        name_b = request.POST.get('name_b', '')
        after_b = request.POST.get('after_b', '')
        caption = request.POST.get('caption', '')

        Books.objects.create(
            name_b=name_b,
            after_b=after_b,
            caption=caption,
        )
        return redirect('list_books')

    return render(request, 'create_book.html')


def delete_books(request, pk):
    books = Books.objects.get(pk=pk)

    if request.method == 'POST':
        books.delete()
        return render(request, 'delete_book.html', {'books': books, 'deleted': True})

    return render(request, 'delete_book.html', {'books': books, 'deleted': False})


def update_books(request, pk):
    books = Books.objects.get(pk=pk)
    if request.method == 'POST':
        books.name_b = request.POST.get('name_b', books.name_b)
        books.after_b = request.POST.get('after_b', books.after_b)
        books.caption = request.POST.get('caption', books.caption)
        books.save()
        return redirect('list_books')
    return render(request, 'update_book.html', {'books': books})
