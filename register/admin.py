from django.contrib import admin
from .models import AddBook
from django.utils.html import format_html

# Register your models here.

class AddBookAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.b_pic.url))

    thumbnail.short_description = 'Car Image'
    list_display = ('id','thumbnail','b_name')
    list_display_links = ('id', 'thumbnail', 'car_title')
    
admin.site.register(AddBook, AddBookAdmin)