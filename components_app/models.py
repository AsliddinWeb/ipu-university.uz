from django.db import models

class SeoSettings(models.Model):
    title = models.CharField(max_length=455)
    description = models.TextField()
    favicon = models.FileField(upload_to='favicon')
    keywords = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Seo Sozlamalari"

class TopHeader(models.Model):
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "Top Header Sozlamalari"

class HeaderLogo(models.Model):
    dark_logo = models.ImageField(upload_to='logos/')
    light_logo = models.ImageField(upload_to='logos/')
    alt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name_plural = "Header Logo Sozlamalari"

class OneHeader(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=755, default="#")
    is_submenu = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "1-Darajali Menyular"

class TwoHeader(models.Model):
    one_header = models.ForeignKey(OneHeader, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=755, default="#")
    is_submenu = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "2-Darajali Menyular"

class ThreeHeader(models.Model):
    one_header = models.ForeignKey(OneHeader, on_delete=models.CASCADE)
    two_header = models.ForeignKey(TwoHeader, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=755, default="#")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "3-Darajali Menyular"

class RightButton(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "O'ng Tomon Tugmacha"

class SocialNetwork(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=755, default="#")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ijtimoiy Tarmoqlar"

class FooterInfo(models.Model):
    dark_logo = models.ImageField(upload_to='logos/')
    light_logo = models.ImageField(upload_to='logos/')

    text = models.TextField()

    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    location = models.CharField(max_length=455)
    copyright = models.TextField()

    class Meta:
        verbose_name_plural = "Footer Sozlamalari"

class FooterLinks(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=455)
    is_useful = models.BooleanField(default=False)

    icon = models.ImageField(upload_to='footer-icons/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Footer Linklar"

class MoreTexts(models.Model):
    qidirish_1 = models.CharField(max_length=255)
    qidirish_2 = models.CharField(max_length=255)
    slider_text = models.CharField(max_length=455, null=True, blank=True)

    news_cap = models.CharField(max_length=255, null=True, blank=True)
    news_title = models.CharField(max_length=255, null=True, blank=True)
    news_more = models.CharField(max_length=255, null=True, blank=True)
    news_korishlar_soni = models.CharField(max_length=255, null=True, blank=True)

    elon_cap = models.CharField(max_length=255, null=True, blank=True)
    elon_title = models.CharField(max_length=255, null=True, blank=True)
    elon_more = models.CharField(max_length=255, null=True, blank=True)

    talim_yonalishlari_cap = models.CharField(max_length=255, null=True, blank=True)
    talim_yonalishlari_title = models.CharField(max_length=255, null=True, blank=True)
    talim_yonalishlari_barcha_yonalishlar = models.CharField(max_length=255, null=True, blank=True)
    talim_yonalishlari_more_link = models.CharField(max_length=255, null=True, blank=True)

    unv_cap = models.CharField(max_length=255, null=True, blank=True)
    unv_title = models.CharField(max_length=255, null=True, blank=True)

    video_cap = models.CharField(max_length=255, null=True, blank=True)
    video_title = models.CharField(max_length=255, null=True, blank=True)

    interaktiv_hizmatlar_cap = models.CharField(max_length=255, null=True, blank=True)
    interaktiv_hizmatlar_title = models.CharField(max_length=255, null=True, blank=True)

    hamkorlar_cap = models.CharField(max_length=255, null=True, blank=True)
    hamkorlar_title = models.CharField(max_length=255, null=True, blank=True)

    footer_foydali_sahifalar = models.CharField(max_length=255, null=True, blank=True)
    footer_interaktiv_hizmatlar = models.CharField(max_length=255, null=True, blank=True)
    footer_boglanish = models.CharField(max_length=255, null=True, blank=True)

    bosh_sahifa = models.CharField(max_length=255, null=True, blank=True)

    qaynoq_yangiliklar_cap = models.CharField(max_length=255, null=True, blank=True)
    qaynoq_yangiliklar_title = models.CharField(max_length=255, null=True, blank=True)

    barcha_yangiliklar = models.CharField(max_length=255, null=True, blank=True)
    ta = models.CharField(max_length=255, null=True, blank=True)
    yangiliklar_text = models.CharField(max_length=255, null=True, blank=True)

    oxirgi_yangiliklar = models.CharField(max_length=255, null=True, blank=True)
    kop_korilgan_yangiliklar = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Qo'shimcha UI matnlar"