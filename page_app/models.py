from ckeditor.fields import RichTextField
from django.db import models
from components_app.models import OneHeader, TwoHeader

# Slug
from django.utils.text import slugify
import random
import string

class Page(models.Model):
    title = models.CharField(max_length=455)
    title_cap = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField()
    slug = models.SlugField(max_length=755, unique=True, blank=True, null=True)

    one_navbar = models.ForeignKey(OneHeader, on_delete=models.SET_NULL, null=True, blank=True)
    two_navbar = models.ForeignKey(TwoHeader, on_delete=models.SET_NULL, null=True, blank=True)
    full_page = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sahifalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.title)
            while Page.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.title + ' ' + random_string)
            self.slug = slug_sample
        super(Page, self).save(*args, **kwargs)