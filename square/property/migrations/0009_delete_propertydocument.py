# Generated by Django 4.2.9 on 2024-04-01 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_rename_current_renter_currentrenter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='propertyDocument',
        ),
    ]
