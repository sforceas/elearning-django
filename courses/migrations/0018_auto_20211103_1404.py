# Generated by Django 3.2.5 on 2021-11-03 14:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_alter_course_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpath',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='learningpath',
            name='icon',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_path',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='video'),
        ),
    ]
