from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(queryset)  # Вывод в консоль для отладки
    #     return queryset


class ProductDetailView(DetailView):
    model = Product


# def contacts_new(request):
#     return render(request, 'catalog/contacts_new.html')

class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts_new.html'
