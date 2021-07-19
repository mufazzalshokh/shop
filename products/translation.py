from modeltranslation.translator import register, TranslationOptions

from products.models import CategoryModel, ProductModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)
