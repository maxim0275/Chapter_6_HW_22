from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('', ProductListView.as_view(), name='products_list_f'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('contacts_new/', ContactTemplateView.as_view(), name='contacts_new')
]
