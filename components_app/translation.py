from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(SeoSettings)
class SeoSettingsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'keywords')

@register(OneHeader)
class OneHeaderTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(TwoHeader)
class TwoHeaderTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(ThreeHeader)
class ThreeHeaderTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(RightButton)
class RightButtonTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(FooterInfo)
class FooterInfoTranslationOptions(TranslationOptions):
    fields = ('text', 'location', 'copyright')

@register(FooterLinks)
class FooterLinksTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(MoreTexts)
class MoreTextsTranslationOptions(TranslationOptions):
    fields = ('qidirish_1', 'qidirish_2', 'slider_text', 'news_cap',
              'news_title', 'news_more', 'elon_cap', 'elon_title', 'elon_more', 'news_korishlar_soni',
              'talim_yonalishlari_cap', 'talim_yonalishlari_title',
              'talim_yonalishlari_barcha_yonalishlar', 'talim_yonalishlari_more_link',
              'unv_cap', 'unv_title', 'video_cap', 'video_title',
              'interaktiv_hizmatlar_cap', 'interaktiv_hizmatlar_title',
              'hamkorlar_cap', 'hamkorlar_title',
              'footer_foydali_sahifalar', 'footer_interaktiv_hizmatlar', 'footer_boglanish',
              'bosh_sahifa', 'qaynoq_yangiliklar_cap', 'qaynoq_yangiliklar_title',
              'barcha_yangiliklar', 'ta', 'yangiliklar_text', 'oxirgi_yangiliklar', 'kop_korilgan_yangiliklar')