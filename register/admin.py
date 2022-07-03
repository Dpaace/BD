from django.contrib import admin
from register.models import AddBook
from django.utils.html import format_html

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.b_pic.url))

    thumbnail.short_description = 'Book Image'
    list_display = ('book_id','thumbnail','b_name')
    list_display_links = ('book_id', 'thumbnail', 'b_name')

admin.site.register(AddBook, BookAdmin)