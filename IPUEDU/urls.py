from django.contrib import admin
from django.urls import path, include

# i18 settings
from django.conf.urls.i18n import i18n_patterns

# Static settings
from django.conf import settings
from django.conf.urls.static import static

from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', home_page, name='home_page'),

    # Pages
    path('page/', include('page_app.urls')),
    path('news/', include('news_app.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)