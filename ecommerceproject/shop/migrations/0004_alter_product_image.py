# Generated by Django 4.1.5 on 2023-09-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_images_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.FileField(upload_to=''),
        ),
    ]
