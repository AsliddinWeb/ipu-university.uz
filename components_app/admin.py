from django.contrib import admin

from .models import *

class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'favicon', 'keywords']
admin.site.register(SeoSettings, SeoSettingsAdmin)

class TopHeaderAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'email', 'text']
admin.site.register(TopHeader, TopHeaderAdmin)

class HeaderLogoAdmin(admin.ModelAdmin):
    list_display = ['alt', 'dark_logo', 'light_logo']
admin.site.register(HeaderLogo, HeaderLogoAdmin)

class OneHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_submenu']
admin.site.register(OneHeader, OneHeaderAdmin)

class TwoHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_submenu', 'one_header']
admin.site.register(TwoHeader, TwoHeaderAdmin)

class ThreeHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'one_header', 'two_header']
admin.site.register(ThreeHeader, ThreeHeaderAdmin)

class RightButtonAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
admin.site.register(RightButton, RightButtonAdmin)

class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'link']
admin.site.register(SocialNetwork, SocialNetworkAdmin)

class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ['dark_logo', 'light_logo', 'text', 'phone_number', 'email', 'location', 'copyright']
admin.site.register(FooterInfo, FooterInfoAdmin)

class FooterLinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_useful', 'icon']
admin.site.register(FooterLinks, FooterLinksAdmin)

class MoreTextsAdmin(admin.ModelAdmin):
    list_display = ['qidirish_1', 'qidirish_2']
admin.site.register(MoreTexts, MoreTextsAdmin)