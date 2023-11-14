from django.contrib import admin
from .models import *

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'cap', 'button_title', 'button_link', 'image']
admin.site.register(Slider, SliderAdmin)

class HomeAboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'one_image', 'two_image', 'three_image', 'cap', 'body', 'button_title', 'button_link']
admin.site.register(HomeAbout, HomeAboutAdmin)

class HomeAboutQulayliklarAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'body']
admin.site.register(HomeAboutQulayliklar, HomeAboutQulayliklarAdmin)

class TalimYonalishlariAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'body']
admin.site.register(TalimYonalishlari, TalimYonalishlariAdmin)

class CounterAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'count', 'is_aniq']
admin.site.register(Counter, CounterAdmin)

class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'lavozimi', 'qabul', 'phone_number', 'email']
admin.site.register(Rahbariyat, RahbariyatAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'link']
admin.site.register(Video, VideoAdmin)

class InteraktivHizmatlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'body', 'button_title', 'button_link']
admin.site.register(InteraktivHizmatlar, InteraktivHizmatlarAdmin)

class HamkorlarAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'button_title', 'button_link']
admin.site.register(Hamkorlar, HamkorlarAdmin)

class MapAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'width', 'height']
admin.site.register(Map, MapAdmin)