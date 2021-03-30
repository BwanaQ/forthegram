# Generated by Django 3.1.7 on 2021-03-30 14:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210330_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_fiis58.jpg', max_length=255, verbose_name='image'),
        ),
    ]
