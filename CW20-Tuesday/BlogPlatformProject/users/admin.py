from django.contrib import admin
from .models import Author
from django.contrib.admin import AdminSite

# Register your models here.

# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
