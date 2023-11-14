from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'title_cap')