from modeltranslation.translator import translator, TranslationOptions

from .models import Product, Shoe, Accessorie, Size, Color


# Model translations
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)


class ShoeTranslationOptions(TranslationOptions):
    fields = ('material_inner', 'material_outer', 'outsole', 'season')


class AccessorieTranslationOptions(TranslationOptions):
    fields = ('type', 'material',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('size_description',)


class ColorTranslationOptions(TranslationOptions):
    fields = ('color',)


# Register models for translation
translator.register(Product, ProductTranslationOptions)
translator.register(Shoe, ShoeTranslationOptions)
translator.register(Accessorie, AccessorieTranslationOptions)
translator.register(Size, SizeTranslationOptions)
translator.register(Color, ColorTranslationOptions)
