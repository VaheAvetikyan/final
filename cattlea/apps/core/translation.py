from modeltranslation.translator import translator, TranslationOptions

from .models import Product, Shoe, Accessorie, Size


# Model translations
class ProductTranslationOptions(TranslationOptions):
    fields = ('color', 'description',)


class ShoeTranslationOptions(TranslationOptions):
    fields = ('sex', 'material_inner', 'material_outer', 'outsole', 'season')


class AccessorieTranslationOptions(TranslationOptions):
    fields = ('type', 'material',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('size_description',)


# Register models for translation
translator.register(Product, ProductTranslationOptions)
translator.register(Shoe, ShoeTranslationOptions)
translator.register(Accessorie, AccessorieTranslationOptions)
translator.register(Size, SizeTranslationOptions)
