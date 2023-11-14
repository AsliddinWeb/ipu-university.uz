from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ckeditor.fields import RichTextField

from hitcount.models import HitCountMixin, HitCount

# Slug
from django.utils.text import slugify
import random
import string

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategoriyalar"

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.title)
            while Category.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.title + ' ' + random_string)
            self.slug = slug_sample
        super(Category, self).save(*args, **kwargs)

STATUS = (
    (0,"Qoralama"),
    (1,"Aktiv")
)
class News(models.Model, HitCountMixin):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=455)
    image = models.ImageField(upload_to='news/')
    image_cap = models.CharField(max_length=455, null=True, blank=True)
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.IntegerField(choices=STATUS, default=0)
    elon_sifatida_belgilash = models.BooleanField(default=False)

    slug = models.SlugField(max_length=755, unique=True, blank=True, null=True)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yangiliklar"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_sample = slugify(self.title)
            while News.objects.filter(slug=slug_sample).exists():
                # Generate a random alphanumeric string of length 6
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                slug_sample = slugify(self.title + ' ' + random_string)
            self.slug = slug_sample
        super(News, self).save(*args, **kwargs)