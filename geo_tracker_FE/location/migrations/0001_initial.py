# Generated by Django 4.0.2 on 2024-07-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetLocation',
            fields=[
                ('device_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('location_latitude', models.CharField(max_length=200)),
                ('location_longitude', models.CharField(max_length=200)),
                ('location_name', models.CharField(max_length=200)),
            ],
        ),
    ]