# Generated by Django 4.2.5 on 2023-09-28 19:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_app', '0002_alter_page_options_page_full_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='body_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='body_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='body_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_en',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_ru',
            field=models.CharField(max_length=455, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='title_uz',
            field=models.CharField(max_length=455, null=True),
        ),
    ]
