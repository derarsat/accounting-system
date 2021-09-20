from django.urls import path

from product import views

urlpatterns = [
    path("category/", views.all_categories, name='category.all'),
    path("seller/", views.all_sellers, name='seller.all'),
    path("add/", views.add_product, name='product.add'),
    path("all/", views.all_products, name='product.all'),
]
