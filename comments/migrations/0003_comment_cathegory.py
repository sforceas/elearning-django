# Generated by Django 3.2.5 on 2021-10-26 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_answercomment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cathegory',
            field=models.CharField(choices=[('comment', 'Comment'), ('question', 'Question')], default='comment', max_length=255),
        ),
    ]
