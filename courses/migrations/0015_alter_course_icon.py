# Generated by Django 3.2.5 on 2021-11-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20211026_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(blank=True, upload_to='media/icons'),
        ),
    ]
