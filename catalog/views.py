from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list_f.html'
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset)  # Вывод в консоль для отладки
    #     return queryset


class ProductDetailView(DetailView):
    model = Product


# def contacts_new(request):
#     return render(request, 'catalog/contacts_new.html')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list_f')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list_f')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products_list_f')


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts_new.html'
