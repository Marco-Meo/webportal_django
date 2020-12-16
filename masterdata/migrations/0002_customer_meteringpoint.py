# Generated by Django 3.1.4 on 2020-12-16 12:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, verbose_name='Firma')),
                ('street', models.CharField(help_text='Strasse und Strassennummer', max_length=100, verbose_name='Strasse')),
                ('zip', models.CharField(max_length=4, verbose_name='PLZ')),
                ('city', models.CharField(max_length=60, verbose_name='Ort')),
            ],
        ),
        migrations.CreateModel(
            name='Meteringpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meteringcode', models.CharField(max_length=33, validators=[django.core.validators.MinLengthValidator(33)], verbose_name='Messpunktnummer')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.customer')),
            ],
        ),
    ]
