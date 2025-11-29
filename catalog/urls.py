from django.urls import path

from catalog.views import product_detail, contacts_view, home_view, index, products_list

app_name = 'catalog'

urlpatterns = [
    path('home/', home_view, name='home_view'),
    path('contacts/', contacts_view, name='contacts_view'),
    path('products_list/', products_list, name='products_list'),
    path('product_detail/<int:product_id>', product_detail, name='product_detail'),
    path('', index)
]
