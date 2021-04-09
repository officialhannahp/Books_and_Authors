from django.shortcuts import render, redirect
from.models import Book, Author

def main(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request,'main.html', context)

def info(request):
    Book.objects.create(
        title=request.POST['title'], 
        desc=request.POST['desc']
    )
    return redirect('/')

def books_id(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        'book' : this_book,
        'all_authors' : Author.objects.all()
    }
    return render(request, "books_id.html", context)

def add_author(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST['author'])
    this_book.authors.add(this_author)
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        'authors' : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def author_info(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect('/authors')

def author_id(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        'author' : this_author,
        'all_books' : Book.objects.all()
    }
    return render(request, "author_id.html", context)

def add_book(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_book = Book.objects.get(id=request.POST['book'])
    this_author.books.add(this_book)
    return redirect(f'/authors/{author_id}')