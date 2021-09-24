from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, redirect
from product.forms import CategoryForm, SellerForm, ProductForm, CurrencyForm
from product.models import Category, Seller, Product, Currency
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
    paginator = Paginator(categories, 3)
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
    paginator = Paginator(sellers, 3)
    try:
        sellers = paginator.page(page)
    except PageNotAnInteger:
        sellers = paginator.page(1)
    except EmptyPage:
        sellers = paginator.page(paginator.num_pages)

    return render(request, 'seller/all.html', {'sellers': sellers, "form": form})


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
    paginator = Paginator(currencies, 3)
    try:
        currencies = paginator.page(page)
    except PageNotAnInteger:
        currencies = paginator.page(1)
    except EmptyPage:
        currencies = paginator.page(paginator.num_pages)

    return render(request, 'currency/all.html', {'currencies': currencies, "form": form})


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
    paginator = Paginator(products, 3)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "product/all.html", {"products": products})
