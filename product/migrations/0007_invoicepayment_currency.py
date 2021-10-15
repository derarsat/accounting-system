# Generated by Django 3.2.7 on 2021-10-15 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_invoicepayment_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicepayment',
            name='Currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.currency'),
            preserve_default=False,
        ),
    ]