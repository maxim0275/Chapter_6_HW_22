from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    # help = 'Добавление тестовых продуктов'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        categories = [
            {'name': 'Основания', 'description': 'Основания для ракеток'}
        ]

        for category in categories:
            add_category = Category(
                name=category['name'],
                description=category['description']
            )
            add_category.save()

        add_category = Category.objects.get(name='Основания')

        products = [
            {'name': 'Основание Peter Korbel', 'description': 'Основание Peter Korbel, Japan', 'category': add_category,
             'price_sale': 15000, 'created_at': '2025-11-22'},
            {'name': 'Основание Timo Boll ALC', 'description': 'Основание TImo Boll, Japan', 'category': add_category,
             'price_sale': 25000, 'created_at': '2025-11-22'},
            {'name': 'Основание Timo Boll ZLC', 'description': 'Основание TImo Boll, Japan', 'category': add_category,
             'price_sale': 28000, 'created_at': '2025-11-22'}
        ]

        for product in products:
            add_product = Product(
                name=product['name'],
                description=product['description'],
                category=product['category'],
                price_sale=product['price_sale'],
                created_at=product['created_at']
            )
            add_product.save()
