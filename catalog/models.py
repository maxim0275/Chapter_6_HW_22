from django.db import models

from users_app.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.CharField(max_length=100, verbose_name="Описание")
    image = models.ImageField(upload_to='images/', verbose_name="Изображение", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price_sale = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(null=True)
    publish_status = models.BooleanField(null=False, verbose_name="Статус публикации")
    owner = models.ForeignKey(User, verbose_name="Владелец продукта",  on_delete=models.PROTECT, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        db_table = 'product'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
