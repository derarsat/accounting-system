# Generated by Django 3.2.7 on 2021-10-18 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_currency_invoicepayment_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(default=' ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='identifier',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='quantitytype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(max_length=1000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=models.CharField(max_length=1000, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='DailyBoxOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('operation', models.CharField(choices=[('1', 'Add'), ('2', 'Take')], max_length=5)),
                ('reason', models.CharField(max_length=255)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.currency')),
            ],
        ),
    ]
