# Generated by Django 5.1.6 on 2025-02-28 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aboutpage'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='main_picture',
            field=models.ForeignKey(blank=True, help_text='Main about picture', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
