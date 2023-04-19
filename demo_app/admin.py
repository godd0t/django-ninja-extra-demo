from django.contrib import admin

from .models import Book, Tag

admin.site.register(Book)
admin.site.register(Tag)
