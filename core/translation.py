from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.admin import TranslationAdmin

from .models import Item, Shoe, Accessorie, Size
from .admin import ShoeAdmin, AccessorieAdmin, SizeAdmin


# Model translations
class ItemTranslationOptions(TranslationOptions):
    fields = ('color',)


class ShoeTranslationOptions(TranslationOptions):
    fields = ('material_inner', 'material_outer', 'outsole', 'season')


class AccessorieTranslationOptions(TranslationOptions):
    fields = ('material',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('size_description',)


# Admin model translations
class ShoeTranslation(TranslationAdmin):
    fields = ('material_inner', 'material_outer', 'outsole', 'season')


class AccessorieTranslation(TranslationAdmin):
    fields = ('material',)


class SizeTranslation(TranslationAdmin):
    fields = ('size_description',)



# Register models for translation
translator.register(Item, ItemTranslationOptions)
translator.register(Shoe, ShoeTranslationOptions)
translator.register(Accessorie, AccessorieTranslationOptions)
translator.register(Size, SizeTranslationOptions)

#translator.register(ShoeAdmin, ShoeTranslation)
#translator.register(AccessorieAdmin, AccessorieTranslation)
#translator.register(SizeAdmin, SizeTranslation)
