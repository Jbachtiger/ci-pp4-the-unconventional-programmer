# Generated by Django 3.2.13 on 2022-07-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmerblog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
