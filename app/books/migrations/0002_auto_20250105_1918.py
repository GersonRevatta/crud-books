# Generated by Django 2.2.28 on 2025-01-05 19:18

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(default=books.models.generate_object_id, editable=False, max_length=24, primary_key=True, serialize=False),
        ),
    ]
