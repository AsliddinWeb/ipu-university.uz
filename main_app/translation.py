from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('cap', 'title', 'button_title', )

@register(HomeAbout)
class HomeAboutTranslationOptions(TranslationOptions):
    fields = ('cap', 'title', 'body', 'button_title')

@register(HomeAboutQulayliklar)
class HomeAboutQulayliklarTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(TalimYonalishlari)
class TalimYonalishlariTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Counter)
class CounterTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Rahbariyat)
class RahbariyatTranslationOptions(TranslationOptions):
    fields = ('name', 'lavozimi', 'qabul', )

@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(InteraktivHizmatlar)
class InteraktivHizmatlarTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'button_title')

@register(Hamkorlar)
class HamkorlarTranslationOptions(TranslationOptions):
    fields = ('title', 'button_title', )