# Generated by Django 3.2.5 on 2021-07-25 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_alter_greeting_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
