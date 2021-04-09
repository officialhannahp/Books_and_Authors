from django.urls import path
from.import views

urlpatterns = [
    path('', views.main),
    path('info', views.info),
    path('books/<int:book_id>', views.books_id),
    path('add_author/<int:book_id>', views.add_author),
    path('authors', views.authors),
    path('author_info', views.author_info),
    path('author/<int:author_id>', views.author_id),
    path('add_book/<int:author_id>', views.add_book)
]