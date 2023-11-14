# Generated by Django 4.2.5 on 2023-09-27 04:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components_app', '0003_alter_footerinfo_options_alter_footerlinks_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=455)),
                ('body', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, max_length=755, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('one_navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='components_app.oneheader')),
                ('two_navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='components_app.twoheader')),
            ],
            options={
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
    ]
