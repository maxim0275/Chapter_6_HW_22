from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, PublishProductView, ProductListViewForCategory

app_name = 'catalog'

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('', ProductListView.as_view(), name='products_list_f'),
    path('product_list_by_category/<int:category_id>', ProductListViewForCategory.as_view(), name='products_list_f1'),
    path('product_detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('contacts_new/', ContactTemplateView.as_view(), name='contacts_new'),
    path('products/<int:product_id>/unpublish/', PublishProductView.as_view(), name='unpublish_product'),
]
