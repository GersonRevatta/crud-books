# Generated by Django 2.2.28 on 2025-01-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20250105_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
