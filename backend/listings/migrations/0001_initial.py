# Generated by Django 4.1.6 on 2023-02-13 09:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('pet_breed', models.CharField(blank=True, max_length=30, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('pet_image1', models.ImageField(blank=True, null=True, upload_to='pet_images/%Y/')),
                ('pet_image2', models.ImageField(blank=True, null=True, upload_to='pet_images/%Y/')),
                ('pet_image3', models.ImageField(blank=True, null=True, upload_to='pet_images/%Y/')),
            ],
        ),
    ]
