# Generated by Django 3.0.6 on 2021-04-10 08:24

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210410_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_albums',
            name='album_name',
            field=models.CharField(max_length=100, validators=[myapp.models.validate_album_name]),
        ),
        migrations.AlterField(
            model_name='musicians',
            name='name',
            field=models.CharField(max_length=50, validators=[myapp.models.validate_name]),
        ),
    ]
