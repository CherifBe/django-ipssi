from django.contrib import admin

# Register your models here.
from .models import Book, BookType, BookStatus

admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(BookStatus)