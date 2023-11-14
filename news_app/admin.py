from django.contrib import admin

from .models import Category, News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'author', 'created_at', 'status']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
admin.site.register(News, NewsAdmin)