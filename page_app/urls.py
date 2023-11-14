from django.urls import path

from .views import PAGE_DETAIL

urlpatterns = [
    path('<slug:slug>/', PAGE_DETAIL, name='page_detail')
]