from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    # help = 'Добавление тестовых продуктов'

    def handle(self, *args, **kwargs):
        cat_1 = Category.objects.get(id=1)
        Product.objects.all().delete()

        products = [
            {'name': 'Основание Peter Korbel', 'description': 'Основание Peter Korbel, Japan', 'category': cat_1,
             'price_sale': 15000, 'created_at': '2025-11-22'},
            {'name': 'Основание Timo Boll ALC', 'description': 'Основание TImo Boll, Japan', 'category': cat_1,
             'price_sale': 25000, 'created_at': '2025-11-22'},
            {'name': 'Основание Timo Boll ZLC', 'description': 'Основание TImo Boll, Japan', 'category': cat_1,
             'price_sale': 28000, 'created_at': '2025-11-22'}
        ]

        for product in products:
            add_product = Product(
                name=product['name'],
                description=product['description'],
                category=cat_1,
                price_sale=product['price_sale'],
                created_at=product['created_at']
            )
            add_product.save()
