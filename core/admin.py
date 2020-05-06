from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Item, Shoe, Accessorie, Size, ShoeSize


# Register your models here.
class ShoeAdmin(admin.ModelAdmin):
    
    list_display = ("model_code", "price", "color", "material_inner", "material_outer", "outsole", "season", "sizes")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price", "sizes"]}),
        ("Specifications", {"fields": ["color", "material_inner", "material_outer", "outsole", "season"]})
    ]


class AccessorieAdmin(admin.ModelAdmin):
    
    list_display = ("model_code", "price", "color", "material")

    fieldsets = [
        ("Model", {"fields": ["model_code", "price"]}),
        ("Specifications", {"fields": ["color", "material"]})
    ]


class SizeAdmin(admin.ModelAdmin):
    list_display = ("size", "size_description")


class ShoeSizeAdmin(admin.ModelAdmin):
    list_display = ("shoe", "size")


admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Accessorie, AccessorieAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(ShoeSize, ShoeSizeAdmin)
