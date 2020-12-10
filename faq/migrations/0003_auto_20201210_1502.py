# Generated by Django 3.1.4 on 2020-12-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_auto_20201209_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='description',
            field=models.CharField(help_text='Hilfestellung beschreiben', max_length=1000, verbose_name='Beschreibung'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='title',
            field=models.CharField(help_text='Titel des FAQ Eintrages', max_length=200, verbose_name='Titel'),
        ),
    ]
