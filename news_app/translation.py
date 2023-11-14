from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'image_cap')
