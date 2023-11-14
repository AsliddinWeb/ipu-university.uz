from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'one_navbar', 'two_navbar', 'created_at', 'full_page']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Page, PageAdmin)