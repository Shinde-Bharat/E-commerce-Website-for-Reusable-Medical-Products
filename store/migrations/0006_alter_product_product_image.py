# Generated by Django 3.2.13 on 2022-07-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
