from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class QuantityType(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.FloatField()

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    stock_price = models.FloatField()
    price = models.FloatField()
    special = models.FloatField()
    expire = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    material = models.ManyToManyField(Material, null=True)
    quantity_type = models.ForeignKey(QuantityType, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    extra_quantity = models.FloatField(null=True)
    barcode = models.CharField(null=True, max_length=30)
    identifier = models.CharField(null=True, max_length=30)
    location = models.CharField(null=True, max_length=30)
    alert_if_lower_than = models.IntegerField(null=True)

    def __str__(self):
        return self.name
