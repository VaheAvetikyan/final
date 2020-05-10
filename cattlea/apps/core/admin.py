from django.contrib import admin
from .models import Product, Shoe, Accessorie, Size
from modeltranslation.admin import TranslationAdmin

# Translate
from django.utils.translation import gettext as _


# Register your models here.

class ShoeInline(admin.TabularInline):
    model = Shoe.sizes.through


class ShoeAdmin(TranslationAdmin):
    
    list_display = ("model_code", "price", "color", "material_inner", "material_outer",
                    "outsole", "season", "description", "available")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price"]}),
        ("Specifications", {"fields": ["color", "material_inner", "material_outer", "outsole", "season", "description"]}),
        ("Availability", {"fields": ["available"]})
    ]

    search_fields = ['price']

    model = Size
    inlines = [ShoeInline, ]


class AccessorieAdmin(TranslationAdmin):
    
    list_display = ("model_code", "price", "color", "material", "description", "available")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price"]}),
        ("Specifications", {"fields": ["color", "material", "description"]}),
        ("Availability", {"fields": ["available"]})
    ]


class SizeAdmin(TranslationAdmin):
    list_display = ("size", "size_description")

'''
class ShoeSizeAdmin(admin.ModelAdmin):
    list_display = ("shoe", "size")
'''

admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Accessorie, AccessorieAdmin)
admin.site.register(Size, SizeAdmin)

admin.site.site_header = _("Admin Panel")
