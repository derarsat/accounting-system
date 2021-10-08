# Generated by Django 3.2.7 on 2021-10-08 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('discount', models.FloatField()),
                ('payed', models.FloatField()),
                ('expected_earn', models.FloatField(blank=True, null=True)),
                ('earn', models.FloatField(blank=True, null=True)),
                ('dept', models.FloatField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.currency')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='desc',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='alert_if_lower_than',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='expire',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='extra_quantity',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.quantitytype'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='InvoiceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('piece_price', models.FloatField()),
                ('total', models.FloatField()),
                ('invoice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.invoice')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.seller'),
        ),
    ]
