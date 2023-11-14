from django.db import models

class Slider(models.Model):
    cap = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Slayderlar"
        ordering = ['-id']

class HomeAbout(models.Model):
    one_image = models.ImageField(upload_to='home-images/')
    two_image = models.ImageField(upload_to='home-images/')
    three_image = models.ImageField(upload_to='home-images/')

    cap = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Asosiy Menyu About"

class HomeAboutQulayliklar(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Home About Qulayliklar"

class TalimYonalishlari(models.Model):
    image = models.ImageField(upload_to='talim-yonalishlari/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.CharField(max_length=455, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Talim Yo'nalishlari"

class Counter(models.Model):
    image = models.ImageField(upload_to='counter/')
    count = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    is_aniq = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Counter"

class Rahbariyat(models.Model):
    image = models.ImageField(upload_to='rahbariyat/')
    name = models.CharField(max_length=455)
    lavozimi = models.TextField()
    qabul = models.TextField()

    # social networks

    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Rahbariyat"

class Video(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='videos')
    link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Video"

class InteraktivHizmatlar(models.Model):
    image = models.ImageField(upload_to='interaktiv-hizmatlar')
    title = models.CharField(max_length=255)
    body = models.TextField()

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Interaktiv Hizmatlar"

class Hamkorlar(models.Model):
    image = models.ImageField(upload_to='hamkorlar')
    title = models.CharField(max_length=255)

    button_title = models.CharField(max_length=255)
    button_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hamkorlar"

class Map(models.Model):
    title = models.CharField(max_length=255)
    link = models.TextField()
    width = models.CharField(max_length=255)
    height = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Xarita Sozlamalari"