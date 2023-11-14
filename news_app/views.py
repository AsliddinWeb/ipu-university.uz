from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from hitcount.views import HitCountDetailView

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from hitcount.models import HitCount

from components_app.models import *
from main_app.models import *
from .models import *

def news_home(request):
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

    # NEWS ------------
    NEWS = News.objects.all()

    NEWS_LEN = len(NEWS)
    NEWS_4 = News.objects.all()[:4]
    POPULAR_NEWS_4 = News.objects.order_by("-hit_count_generic__hits")[:4]

    # Search
    search_post = request.GET.get('search')
    if search_post:
        posts = News.objects.filter(Q(title__icontains=search_post) & Q(body__icontains=search_post))
    else:
        # If not searched, return default posts
        posts = NEWS

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

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

        # NEWS
        'NEWS': NEWS,
        'NEWS_LEN': NEWS_LEN,
        'items': items,

        'NEWS_4': NEWS_4,
        'POPULAR_NEWS_4': POPULAR_NEWS_4,
    }
    return render(request, 'page/news_home.html', ctx)

class NewsDetailView(HitCountDetailView):
    model = News
    count_hit = True
    template_name = 'page/news_detail.html'
    context_object_name = 'NEWS'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        # NEWS-------------
        # NEWS = get_object_or_404(News, slug=slug)
        ALL_NEWS = News.objects.all()[:3]

        context['TOP_HEADER'] = TOP_HEADER
        context['SOCIAL_NETWORKS'] = SOCIAL_NETWORKS
        context['HEADER_LOGO'] = HEADER_LOGO

        context['ONE_HEADER'] = ONE_HEADER
        context['TWO_HEADER'] = TWO_HEADER
        context['THREE_HEADER'] = THREE_HEADER

        context['MORE_TEXTS'] = MORE_TEXTS
        context['RIGHT_BUTTON'] = RIGHT_BUTTON
        context['SEO_SETTINGS'] = SEO_SETTINGS
        context['FOOTER_INFO'] = FOOTER_INFO
        context['FOOTER_FOYDALI_LINKS'] = FOOTER_FOYDALI_LINKS
        context['FOOTER_INTERAKTIV_LINKS'] = FOOTER_INTERAKTIV_LINKS

        # NEWS
        # context['NEWS'] = NEWS
        context['ALL_NEWS'] = ALL_NEWS

        return context

# def news_detail(request, slug):
#     # UI Requirements
#     TOP_HEADER = TopHeader.objects.last()
#     SOCIAL_NETWORKS = SocialNetwork.objects.all()
#     HEADER_LOGO = HeaderLogo.objects.last()
#     SEO_SETTINGS = SeoSettings.objects.last()
#
#     ONE_HEADER = OneHeader.objects.all()
#     TWO_HEADER = TwoHeader.objects.all()
#     THREE_HEADER = ThreeHeader.objects.all()
#
#     MORE_TEXTS = MoreTexts.objects.last()
#     RIGHT_BUTTON = RightButton.objects.last()
#     FOOTER_INFO = FooterInfo.objects.last()
#     FOOTER_FOYDALI_LINKS = FooterLinks.objects.filter(is_useful=True)
#     FOOTER_INTERAKTIV_LINKS = FooterLinks.objects.filter(is_useful=False)
#
#     # NEWS-------------
#     NEWS = get_object_or_404(News, slug=slug)
#     ALL_NEWS = News.objects.all()[:3]
#
#
#     ctx = {
#         # UI Requirements
#         'TOP_HEADER': TOP_HEADER,
#         'SOCIAL_NETWORKS': SOCIAL_NETWORKS,
#         'HEADER_LOGO': HEADER_LOGO,
#
#         'ONE_HEADER': ONE_HEADER,
#         'TWO_HEADER': TWO_HEADER,
#         'THREE_HEADER': THREE_HEADER,
#
#         'MORE_TEXTS': MORE_TEXTS,
#         'RIGHT_BUTTON': RIGHT_BUTTON,
#         'SEO_SETTINGS': SEO_SETTINGS,
#         'FOOTER_INFO': FOOTER_INFO,
#         'FOOTER_FOYDALI_LINKS': FOOTER_FOYDALI_LINKS,
#         'FOOTER_INTERAKTIV_LINKS': FOOTER_INTERAKTIV_LINKS,
#
#         # NEWS
#         'NEWS': NEWS,
#         'ALL_NEWS': ALL_NEWS,
#     }
#
#     # hitcount logic
#     hit_count = get_hitcount_model().objects.get_for_object(NEWS)
#     hits = hit_count.hits
#     hitcontext = ctx['hitcount'] = {'pk': hit_count.pk, 'object': hit_count}
#     hit_count_response = HitCountMixin.hit_count(request, hit_count)
#     if hit_count_response.hit_counted:
#         hits = hits + 1
#         hitcontext['hit_counted'] = hit_count_response.hit_counted
#         hitcontext['hit_message'] = hit_count_response.hit_message
#         hitcontext['total_hits'] = hits
#
#     return render(request, 'page/news_detail.html', ctx)


def search_page(request):
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

    # NEWS ------------
    NEWS = News.objects.all()

    NEWS_LEN = len(NEWS)
    NEWS_4 = News.objects.all()[:4]
    POPULAR_NEWS_4 = News.objects.all()[:4]

    # Search
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) & Q(content__icontains=search_post))
    else:
        # If not searched, return default posts
        posts = Post.objects.all().order_by("-date_created")

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

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

        # NEWS
        'NEWS': NEWS,
        'NEWS_LEN': NEWS_LEN,
        'items': items,

        'NEWS_4': NEWS_4,
        'POPULAR_NEWS_4': POPULAR_NEWS_4,
    }
    return render(request, 'page/news_home.html', ctx)