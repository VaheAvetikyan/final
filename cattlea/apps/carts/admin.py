from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):

    list_display = ("user", "product", "size", "date_added")

    # fieldsets = [
    #     ("User", {"fields": ["user"]}),
    #     ("Product", {"fields": ["product", "size"]})
    # ]

    ordering = ['date_added']
    search_fields = ['user']


# Register your models here.
admin.site.register(Cart, CartAdmin)
