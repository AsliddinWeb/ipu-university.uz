from django.shortcuts import render

from components_app.models import *
from main_app.models import *
from news_app.models import *

def home_page(request):
    # UI Requirements
    TOP_HEADER = TopHeader.objects.last()
    SOCIAL_NETWORKS = SocialNetwork.objects.all()
    HEADER_LOGO = HeaderLogo.objects.last()
    SEO_SETTINGS = SeoSettings.objects.last()

    ONE_HEADER = OneHeader.objects.all()
    TWO_HEADER = TwoHeader.objects.all()
    THREE_HEADER = ThreeHeader.objects.all()

    MORE_TEXTS = MoreTexts.objects.last()
    RIGHT_BUTTON = RightButton.objects.last()
    FOOTER_INFO = FooterInfo.objects.last()
    FOOTER_FOYDALI_LINKS = FooterLinks.objects.filter(is_useful=True)
    FOOTER_INTERAKTIV_LINKS = FooterLinks.objects.filter(is_useful=False)

    # Main requirements
    SLIDERS = Slider.objects.all()[:3]
    HOME_ABOUT = HomeAbout.objects.last()
    HOME_ABOUT_QULAYLIKLAR = HomeAboutQulayliklar.objects.all()
    NEWS = News.objects.filter(elon_sifatida_belgilash=False, status=1)
    ELONLAR = News.objects.filter(elon_sifatida_belgilash=True, status=1)[:4]
    ELONLAR3 = News.objects.filter(elon_sifatida_belgilash=True, status=1)[1:4]
    YONALISHLAR = TalimYonalishlari.objects.all()
    COUNTER = Counter.objects.all()
    RAHBARIYAT = Rahbariyat.objects.all()
    VIDEO = Video.objects.last()
    INTERAKTIV_HIZMATLAR = InteraktivHizmatlar.objects.all()
    HAMKORLAR = Hamkorlar.objects.all()
    MAP = Map.objects.last()



    ctx = {
        # UI Requirements
        'TOP_HEADER': TOP_HEADER,
        'SOCIAL_NETWORKS': SOCIAL_NETWORKS,
        'HEADER_LOGO': HEADER_LOGO,

        'ONE_HEADER': ONE_HEADER,
        'TWO_HEADER': TWO_HEADER,
        'THREE_HEADER': THREE_HEADER,

        'MORE_TEXTS': MORE_TEXTS,
        'RIGHT_BUTTON': RIGHT_BUTTON,
        'SEO_SETTINGS': SEO_SETTINGS,
        'FOOTER_INFO': FOOTER_INFO,
        'FOOTER_FOYDALI_LINKS': FOOTER_FOYDALI_LINKS,
        'FOOTER_INTERAKTIV_LINKS': FOOTER_INTERAKTIV_LINKS,

        # Main requirements
        'SLIDERS': SLIDERS,
        'HOME_ABOUT': HOME_ABOUT,
        'HOME_ABOUT_QULAYLIKLAR': HOME_ABOUT_QULAYLIKLAR,
        'NEWS': NEWS,
        'ELONLAR': ELONLAR,
        'ELONLAR3': ELONLAR3,
        'YONALISHLAR': YONALISHLAR,
        'COUNTER': COUNTER,
        'RAHBARIYAT': RAHBARIYAT,
        'VIDEO': VIDEO,
        'INTERAKTIV_HIZMATLAR': INTERAKTIV_HIZMATLAR,
        'HAMKORLAR': HAMKORLAR,
        'MAP': MAP

    }
    return render(request, 'Main/index.html', ctx)