# Generated by Django 4.2.5 on 2023-11-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components_app', '0021_moretexts_footer_boglanish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moretexts',
            name='news_korishlar_soni',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='news_korishlar_soni_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='news_korishlar_soni_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='news_korishlar_soni_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
