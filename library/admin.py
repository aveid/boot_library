from django.contrib import admin

from library.models import Author, Book, Image


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', ]


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "isbn", "author"]


admin.site.register(Book, BookAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]


admin.site.register(Image, ImageAdmin)
