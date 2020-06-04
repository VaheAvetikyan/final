from django.contrib import admin
from .models import OrderItem, Order


class ItemsInLine(admin.TabularInline):
    model = Order.items.through


class OrderAdmin(admin.ModelAdmin):

    list_display = ("user", "ordered_date", "ordered", "shipping_address", "being_delivered", "received")

    inlines = [ItemsInLine, ]


class OrderItemAdmin(admin.ModelAdmin):

    list_display = ('user', 'item', 'size', 'color', 'quantity', 'price')


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
