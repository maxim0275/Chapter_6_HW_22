from django import forms
from .models import Product

class ProductListView():
    model = Product
    template_name = 'product_list_f.html'
    context_object_name = 'products_ctx'