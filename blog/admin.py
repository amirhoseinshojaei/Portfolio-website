from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin (admin.ModelAdmin):

    list_display = [
        'title',
        'author',
        'date',
        'update_at'
    ]

    list_filter = [
        'author',
        'date',
        'update_at'
    ]

admin.site.register (Blog , BlogAdmin)