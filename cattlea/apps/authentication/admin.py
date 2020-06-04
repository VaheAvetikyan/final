from django.contrib import admin
from .models import User, Address


class UserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name", "password", "is_staff", "is_active", "date_joined")


class AddressAdmin(admin.ModelAdmin):

    list_display = ("city", "street_address", "apartment_address", "zip")


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Address, AddressAdmin)
