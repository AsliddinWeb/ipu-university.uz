# Generated by Django 4.2.5 on 2023-11-06 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_news_elon_sifatida_belgilash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.IntegerField(choices=[(0, 'Qoralama'), (1, 'Aktiv')], default=0),
        ),
    ]
