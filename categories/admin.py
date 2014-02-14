from categories.models import Category
from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name")

admin.site.register(Category)

