from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Product, Shoe, Accessorie, Size, Color


# Translate
from django.utils.translation import gettext as _


# Register your models here.

class ShoeInline(admin.TabularInline):
    model = Shoe.sizes.through


class ColorInline(admin.TabularInline):
    model = Color.colors.through


class ShoeAdmin(TranslationAdmin):
    
    list_display = ("model_code", "price", "image", "material_inner", "material_outer",
                    "outsole", "season", "description", "available")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price", "image"]}),
        ("Specifications", {"fields": ["material_inner", "material_outer", "outsole", "season", "description"]}),
        ("Availability", {"fields": ["available"]})
    ]

    search_fields = ['price']

    model = Size
    inlines = [ShoeInline, ColorInline]


class AccessorieAdmin(TranslationAdmin):
    
    list_display = ("model_code", "price", "image", "material", "description", "available")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price", "image"]}),
        ("Specifications", {"fields": ["material", "description"]}),
        ("Availability", {"fields": ["available"]})
    ]

    inlines = [ColorInline, ]

class SizeAdmin(TranslationAdmin):
    list_display = ("size", "size_description")


class ColorAdmin(TranslationAdmin):
    list_display = ("color", )


admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Accessorie, AccessorieAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Color, ColorAdmin)

admin.site.site_header = _("Admin Panel")
