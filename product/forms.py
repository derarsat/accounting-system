from django.forms import ModelForm

from product.models import Category, Seller, Product, Currency, Material


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
