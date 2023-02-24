from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.

from django.contrib import admin


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )


@admin.register(StockInfo)
class StockInfoAdmin(admin.ModelAdmin):
    list_display = ["symbol", "sector", "long_name"]
    list_per_page = 20
    ordering = ["symbol", "long_name"]
    search_fields = ["symbol__istartswith"]
