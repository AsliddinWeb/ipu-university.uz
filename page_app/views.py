from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Page
from components_app.models import *

def PAGE_DETAIL(request, slug):
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

    # PAGE
    PAGE = get_object_or_404(Page, slug=slug)

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

        # PAGE
        'PAGE': PAGE,
    }
    return render(request, 'page/page.html', ctx)