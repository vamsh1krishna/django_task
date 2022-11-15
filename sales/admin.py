from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Products

@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ('region','city','category','product','quantity','unit_price','ordered_date')
    ...
# Register your models here.
