from django.urls import path

from product import views

urlpatterns = [
    path("sharmoota/", views.all_categories, name='category.all'),
    path("seller/", views.all_sellers, name='seller.all'),
    path("quantity_types/", views.all_quantity_types, name='quantity_type.all'),
    path("currency/", views.all_currencies, name='currency.all'),
    path("material/", views.all_materials, name='material.all'),
    path("invoice/add", views.add_invoice, name='invoice.add'),
    path("product/add/", views.add_product, name='product.add'),
    path("product/autocomplete/", views.product_autocomplete, name='product.autocomplete'),
    path("", views.all_products, name='product.all'),
]
