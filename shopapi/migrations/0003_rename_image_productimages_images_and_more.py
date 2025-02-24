# Generated by Django 5.1.6 on 2025-02-20 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapi', '0002_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimages',
            old_name='image',
            new_name='images',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='reviews_qty',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stars_qty',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
