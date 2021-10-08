# Generated by Django 3.2.7 on 2021-10-08 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211008_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.invoice'),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]