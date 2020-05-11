from django.contrib import admin
from .models import Order, Address


class ItemsInLine(admin.TabularInline):
    model = Order.items.through


class OrderAdmin(admin.ModelAdmin):

    list_display = ("user", "ordered_date", "ordered", "shipping_address", "being_delivered", "received")

    inlines = [ItemsInLine, ]


class AddressAdmin(admin.ModelAdmin):

    list_display = ("user", "city", "street_address", "apartment_address", "zip")


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
