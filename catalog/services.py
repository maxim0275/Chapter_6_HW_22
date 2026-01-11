from django.core.cache import cache

from config.settings import CACHE_ENABLED
from catalog.models import Product


def get_products_from_cache():
    """ Получает данные из кеша. Если нужны данных нет в кеше, то продукты берутся из базы данных"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class ProductsService:

    @staticmethod
    def get_products_by_category(category):
        products = Product.objects.filter(category=category)
        print("Products in category:", products)  # Отладочный вывод
        return products