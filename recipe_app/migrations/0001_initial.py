# Generated by Django 5.1 on 2024-08-27 06:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('conform_password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Non_veg_recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('difficulty_level', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/recipe_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Veg_recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cooking_time', models.IntegerField()),
                ('difficulty_level', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/recipe_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
