# Generated by Django 4.1.6 on 2023-02-22 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0008_remove_pet_qr_code_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med', models.JSONField(null=True)),
                ('pet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='listings.pet')),
            ],
        ),
    ]