# Generated by Django 4.2.14 on 2024-07-30 05:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('email', models.EmailField(blank=True, max_length=225, null=True, unique=True)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='gallery')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OurWonderfulPlants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='plants')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='sitelogo')),
                ('site_name', models.CharField(blank=True, max_length=225, null=True)),
                ('site_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('site_subname', models.CharField(blank=True, max_length=225, null=True)),
                ('site_image', models.ImageField(blank=True, null=True, upload_to='siteimage')),
                ('about_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('satisfaction', models.IntegerField(blank=True, default=0, null=True)),
                ('freedelivery', models.IntegerField(blank=True, default=0, null=True)),
                ('storelocators', models.IntegerField(blank=True, default=0, null=True)),
                ('adress', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=225, null=True)),
                ('contactimg', models.ImageField(blank=True, null=True, upload_to='contactimg')),
                ('map', models.ImageField(blank=True, null=True, upload_to='map')),
                ('search_icon', models.ImageField(blank=True, null=True, upload_to='search_icon')),
                ('loading', models.ImageField(blank=True, null=True, upload_to='loading')),
                ('about_bg', models.ImageField(blank=True, null=True, upload_to='about_bg')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
