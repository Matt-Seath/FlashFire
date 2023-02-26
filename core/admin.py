from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin


@admin.register(StockInfo)
class StockInfoAdmin(admin.ModelAdmin):
    list_display = ["symbol", "sector", "long_name"]
    list_per_page = 20
    ordering = ["symbol", "long_name"]
    search_fields = ["symbol__istartswith"]
