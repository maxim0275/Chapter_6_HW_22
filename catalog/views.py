from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseForbidden, request
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    login_url = reverse_lazy('users_app:login')


# def contacts_new(request):
#     return render(request, 'catalog/contacts_new.html')

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list_f')
    login_url = reverse_lazy('users_app:login')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list_f')
    login_url = reverse_lazy('users_app:login')
    permission_required = 'catalog.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:products_list_f')
    login_url = reverse_lazy('users_app:login')
    permission_required = 'catalog.delete_product'


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts_new.html'


class PublishProductView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:login')

    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        # Логика изменения статуса
        product.publish_status = False
        product.save()

        return redirect('catalog:products_list')
