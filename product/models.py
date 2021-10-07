from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=300, null=True, blank=False)

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
    desc = models.CharField(max_length=300, null=True, blank=False)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=300, null=True, unique=True, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    stock_price = models.FloatField()
    price = models.FloatField()
    special = models.FloatField()
    expire = models.DateField(null=True, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    material = models.ManyToManyField(Material)
    quantity_type = models.ForeignKey(QuantityType, on_delete=models.SET_NULL, null=True)
    quantity = models.FloatField()
    extra_quantity = models.FloatField(null=True, default=0)
    barcode = models.CharField(null=True, max_length=30, blank=False)
    identifier = models.CharField(null=True, max_length=30, blank=False)
    location = models.CharField(null=True, max_length=30, blank=False)
    alert_if_lower_than = models.IntegerField(null=True)
    image = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    total = models.FloatField()
    payed = models.FloatField()
    expected_earn = models.FloatField()
    earn = models.FloatField()
    dept = models.FloatField()
    date_published = models.DateTimeField(auto_now_add=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)


class InvoiceProduct(models.Model):
    product = models.ManyToManyField(Invoice)
    quantity = models.FloatField()
    piece_price = models.FloatField()
    total = models.FloatField()
