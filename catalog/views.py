from django.shortcuts import render
from catalog.models import Product


def home_view(request):
    return render(request, 'catalog/home.html')


def contacts_view(request):
    return render(request, 'catalog/contacts.html')


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/products_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)


def index(request):
    return render(request, 'catalog/base.html')
