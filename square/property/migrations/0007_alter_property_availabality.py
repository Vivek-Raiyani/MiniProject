# Generated by Django 4.2.9 on 2024-03-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_rename_type_pricing_price_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='availabality',
            field=models.BooleanField(default=True),
        ),
    ]
