from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ("email", "first_name", "last_name", "password", "is_staff", "is_active", "date_joined")


# Register your models here.
admin.site.register(User, UserAdmin)
