from django.contrib import admin
from .models import Cart


class ItemsInLine(admin.TabularInline):
    model = Cart.items.through


class CartAdmin(admin.ModelAdmin):

    list_display = ("user",)
    search_fields = ['user']

    inlines = [ItemsInLine, ]


# Register your models here.
admin.site.register(Cart, CartAdmin)
