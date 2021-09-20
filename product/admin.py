from django.contrib import admin

# Register your models here.
from product.models import Product, Category, Seller, QuantityType, Material, Currency

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(QuantityType)
admin.site.register(Material)
admin.site.register(Currency)
