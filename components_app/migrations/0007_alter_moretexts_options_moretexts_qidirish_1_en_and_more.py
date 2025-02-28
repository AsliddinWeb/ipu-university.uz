# Generated by Django 4.2.5 on 2023-11-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components_app', '0006_moretexts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moretexts',
            options={'verbose_name_plural': "Qo'shimcha UI matnlar"},
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_1_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_1_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_1_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_2_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_2_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moretexts',
            name='qidirish_2_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
