from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = 'catalog'

urlpatterns = [
    path('list', ProductListView.as_view(), name='products_list'),
    path('list_f', ProductListView.as_view(), name='products_list_f'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_detail_f/<int:pk>', ProductDetailView.as_view(), name='product_detail_f'),
    path('contacts_new/', ContactTemplateView.as_view(), name='contacts_new')
]
