from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts_new/', ContactTemplateView.as_view(), name='contacts_new')
]
