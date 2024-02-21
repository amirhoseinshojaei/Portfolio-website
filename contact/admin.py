from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin (admin.ModelAdmin):

    list_display = [
        'name',
        'email',
        'phone',
        'message'
    ]

    list_filter = [
        'email',
        'name',
        'phone'
    ]

admin.site.register (Contact,ContactAdmin)