# Generated by Django 3.2.7 on 2021-10-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(default=' ', max_length=30, null=True),
        ),
    ]
