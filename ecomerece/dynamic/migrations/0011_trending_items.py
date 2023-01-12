# Generated by Django 4.0.6 on 2022-08-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0010_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_photo', models.ImageField(upload_to='media')),
                ('discount', models.CharField(blank=True, max_length=200, null=True)),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('specification', models.CharField(blank=True, max_length=200, null=True)),
                ('short_description', models.TextField(blank=True, max_length=200, null=True)),
                ('actual_price', models.CharField(blank=True, max_length=200, null=True)),
                ('discount_price', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]