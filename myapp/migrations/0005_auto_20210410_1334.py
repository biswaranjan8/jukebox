# Generated by Django 3.0.6 on 2021-04-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210410_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicians',
            name='musician_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]