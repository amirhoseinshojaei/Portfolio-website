from django.contrib import admin
from .models import Service
# Register your models here.

class ServicesAdmin (admin.ModelAdmin):

    list_display = [
        'title',
        'date',
        'user',
    ]

    list_filter = [
        'title',
        'date',
        'user'
    ]

    date_hierarchy = 'date'

admin.site.register(Service,ServicesAdmin)