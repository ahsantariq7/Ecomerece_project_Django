# Generated by Django 4.0.6 on 2022-08-19 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0003_shop_by_brand_brand_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_By_Brand1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Shop_By_Brand',
        ),
    ]
