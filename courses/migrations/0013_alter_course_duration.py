# Generated by Django 3.2.5 on 2021-09-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_learningpath_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(blank=True),
        ),
    ]
