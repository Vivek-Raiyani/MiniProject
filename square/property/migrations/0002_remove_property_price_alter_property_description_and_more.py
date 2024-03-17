# Generated by Django 4.2.9 on 2024-03-17 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='typeOfProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Residential'), (2, 'Commercial'), (3, 'Storts Ground'), (4, 'Apartment'), (5, 'Villa'), (6, 'Office'), (7, 'Shop'), (8, 'Warehouse'), (9, 'Factory'), (10, 'Hotel'), (11, 'Cottage'), (12, 'Farmhouse'), (13, 'Cabin'), (14, 'Penthouse'), (15, 'Swimming Pool'), (16, 'Clubhouse'), (17, 'Garden'), (18, 'Gym'), (19, 'Cinema'), (20, 'Cafe'), (21, 'Stadium'), (22, 'Room')], default=1)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='propertyVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_video', models.FileField(upload_to='property_videos')),
                ('video2', models.FileField(blank=True, null=True, upload_to='property_videos')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='propertyLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=6)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='propertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_image', models.ImageField(upload_to='property_images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='property_images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='property_images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='property_images')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='property_images')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='propertyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_document', models.FileField(upload_to='property_documents')),
                ('document2', models.FileField(blank=True, null=True, upload_to='property_documents')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
            ],
        ),
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'PerDay'), (2, 'PerWeek'), (3, 'Monthly'), (4, 'Yearly')], default=1)),
                ('price', models.FloatField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.typeofproperty')),
            ],
        ),
        migrations.CreateModel(
            name='current_renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]