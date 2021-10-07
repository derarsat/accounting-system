import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from product.forms import CategoryForm, SellerForm, ProductForm, CurrencyForm, MaterialForm, QuantityTypeForm
from product.models import Category, Seller, Product, Currency, Material, QuantityType
from turbo.settings import LOGIN_URL


# Categories
@login_required(login_url=LOGIN_URL)
def all_categories(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        method = request.POST.get("method").lower()
        if method == "post":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Category added successfully.')
                return redirect("category.all")
        elif method == "delete":
            category_id = request.POST.get("category_id")
            Category.objects.get(pk=category_id).delete()
            messages.add_message(request, messages.WARNING, 'Category deleted successfully.')
            return redirect("category.all")
        elif method == "put":
            category_id = request.POST.get("category_id")
            category_name = request.POST.get("name")
            category_desc = request.POST.get("desc")
            category_exists = Category.objects.filter(name=category_name).exclude(pk=category_id)
            if not category_exists:
                category = Category.objects.get(pk=category_id)
                category.name = category_name
                category.desc = category_desc
                category.save()
                messages.add_message(request, messages.SUCCESS, 'Category updated successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Category data exists')

            return redirect("category.all")
            # Get method
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(categories, 15)
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    return render(request, 'category/all.html', {'categories': categories, "form": form})


# Sellers
@login_required(login_url=LOGIN_URL)
def all_sellers(request):
    # post method
    if request.method == 'POST':
        method = request.POST.get("method").lower()
        if method == "post":
            form = SellerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Seller added successfully.')
                return redirect("seller.all")
        elif method == "delete":
            seller_id = request.POST.get("seller_id")
            Seller.objects.get(pk=seller_id).delete()
            messages.add_message(request, messages.WARNING, 'Seller deleted successfully.')
            return redirect("seller.all")
        elif method == "put":
            seller_id = request.POST.get("seller_id")
            seller_name = request.POST.get("name")
            seller_phone = request.POST.get("phone")
            seller_exists = Seller.objects.filter(name=seller_name).exclude(pk=seller_id)
            if not seller_exists:
                seller = Seller.objects.get(pk=seller_id)
                seller.name = seller_name
                seller.phone = seller_phone
                seller.save()
                messages.add_message(request, messages.SUCCESS, 'Seller updated successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Seller data exists')

            return redirect("seller.all")
    # Get method
    else:
        form = SellerForm()
    sellers = Seller.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(sellers, 15)
    try:
        sellers = paginator.page(page)
    except PageNotAnInteger:
        sellers = paginator.page(1)
    except EmptyPage:
        sellers = paginator.page(paginator.num_pages)

    return render(request, 'seller/all.html', {'sellers': sellers, "form": form})


@login_required(login_url=LOGIN_URL)
def all_quantity_types(request):
    if request.method == 'POST':
        method = request.POST.get("method").lower()
        if method == "post":
            form = QuantityTypeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Quantity Type added successfully.')
                return redirect("quantity_type.all")
        elif method == "delete":
            quantity_type_id = request.POST.get("quantity_type_id")
            QuantityType.objects.get(pk=quantity_type_id).delete()
            messages.add_message(request, messages.WARNING, 'Quantity Type deleted successfully.')
            return redirect("quantity_type.all")
        elif method == "put":
            quantity_type_id = request.POST.get("quantity_type_id")
            quantity_type_name = request.POST.get("name")
            quantity_type_value = request.POST.get("value")
            quantity_type_exists = QuantityType.objects.filter(name=quantity_type_name).exclude(pk=quantity_type_id)
            if not quantity_type_exists:
                quantity_type = QuantityType.objects.get(pk=quantity_type_id)
                quantity_type.name = quantity_type_name
                quantity_type.value = quantity_type_value
                quantity_type.save()
                messages.add_message(request, messages.SUCCESS, 'Quantity Type updated successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Quantity Type data exists')

            return redirect("quantity_type.all")
            # Get method
    else:
        form = QuantityTypeForm()
        quantity_types = QuantityType.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(quantity_types, 15)
    try:
        quantity_types = paginator.page(page)
    except PageNotAnInteger:
        quantity_types = paginator.page(1)
    except EmptyPage:
        quantity_types = paginator.page(paginator.num_pages)
    return render(request, 'quantity_type/all.html', {'quantity_types': quantity_types, "form": form})


# Currencies
@login_required(login_url=LOGIN_URL)
def all_currencies(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        method = request.POST.get("method").lower()
        if method == "post":
            form = CurrencyForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Currency added successfully.')
                return redirect("currency.all")
        elif method == "delete":
            currency_id = request.POST.get("currency_id")
            Currency.objects.get(pk=currency_id).delete()
            messages.add_message(request, messages.WARNING, 'Currency deleted successfully.')
            return redirect("currency.all")
        elif method == "put":
            currency_id = request.POST.get("currency_id")
            currency_name = request.POST.get("name")
            currency_value = request.POST.get("value")
            currency_rate = request.POST.get("rate")
            currency_exists = Currency.objects.filter(name=currency_name).exclude(pk=currency_id)
            if not currency_exists:
                currency = Currency.objects.get(pk=currency_id)
                currency.name = currency_name
                currency.value = currency_value
                currency.rate = currency_rate
                currency.save()
                messages.add_message(request, messages.SUCCESS, 'Currency updated successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Currency data exists')

            return redirect("currency.all")
            # Get method
    else:
        form = CurrencyForm()
    currencies = Currency.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(currencies, 15)
    try:
        currencies = paginator.page(page)
    except PageNotAnInteger:
        currencies = paginator.page(1)
    except EmptyPage:
        currencies = paginator.page(paginator.num_pages)

    return render(request, 'currency/all.html', {'currencies': currencies, "form": form})


# Materials
@login_required(login_url=LOGIN_URL)
def all_materials(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        method = request.POST.get("method").lower()
        if method == "post":
            form = MaterialForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Material added successfully.')
                return redirect("material.all")
        elif method == "delete":
            material_id = request.POST.get("material_id")
            Material.objects.get(pk=material_id).delete()
            messages.add_message(request, messages.WARNING, 'Material deleted successfully.')
            return redirect("material.all")
        elif method == "put":
            material_id = request.POST.get("material_id")
            material_name = request.POST.get("name")
            material_desc = request.POST.get("desc")
            material_exists = Material.objects.filter(name=material_name).exclude(pk=material_id)
            if not material_exists:
                material = Material.objects.get(pk=material_id)
                material.name = material_name
                material.desc = material_desc
                material.save()
                messages.add_message(request, messages.SUCCESS, 'Material updated successfully.')
            else:
                messages.add_message(request, messages.WARNING, 'Material data exists')

            return redirect("material.all")
            # Get method
    else:
        form = MaterialForm()
    materials = Material.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(materials, 15)
    try:
        materials = paginator.page(page)
    except PageNotAnInteger:
        materials = paginator.page(1)
    except EmptyPage:
        materials = paginator.page(paginator.num_pages)

    return render(request, 'material/all.html', {'materials': materials, "form": form})


@login_required(login_url=LOGIN_URL)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product added successfully.')
            return redirect("product.all")
    else:
        form = ProductForm()
        return render(request, 'product/add.html', {"form": form})


@login_required(login_url=LOGIN_URL)
def all_products(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "product/all.html", {"products": products})


@csrf_exempt
# @login_required(login_url=LOGIN_URL)
def add_invoice(request):
    if request.method == "POST":
        data = json.loads(request.POST.get("data"))
        return JsonResponse(data["activeProducts"], safe=False)
    else:
        return render(request, "invoice/add.html")


def product_autocomplete(request):
    query = request.POST.get("query")
    if len(query) > 2:
        products = Product.objects.filter(
            Q(name__contains=query) |
            Q(material__name__contains=query) |
            Q(identifier__contains=query) |
            Q(barcode__contains=query)
        )

        for product in products:
            print(product.category.name)

        products = serializers.serialize("json", products)
        result = {"result": products}
        return JsonResponse(result)


def get_currencies(request):
    result = Currency.objects.all()
    result = serializers.serialize("json", result)
    result = {"result": result}
    return JsonResponse(result)


def get_sellers(request):
    result = Seller.objects.all()
    result = serializers.serialize("json", result)
    result = {"result": result}
    return JsonResponse(result)

