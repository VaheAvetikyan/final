from django.contrib import admin
from .models import Cart, CartItem


class ItemsInLine(admin.TabularInline):
    model = Cart.items.through


class CartAdmin(admin.ModelAdmin):

    list_display = ("user",)
    search_fields = ['user']

    inlines = [ItemsInLine, ]


class CartItemAdmin(admin.ModelAdmin):

    list_display = ('user', 'item', 'size', 'color', 'quantity', 'date_added')


# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
