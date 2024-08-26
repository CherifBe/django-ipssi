from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

def index(request):
    return HttpResponse('<h1>Book index page</h1>')

def getBooks(request):
    books = Book.objects.all()
    books_html = "<ul>"
    for book in books:
        books_html += "<li>" + book.name + "</li>"
    books_html += "</ul>"

    return HttpResponse(books_html)
