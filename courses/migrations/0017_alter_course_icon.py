# Generated by Django 3.2.5 on 2021-11-03 12:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_courseprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
