from django.db import models


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
    created_at = models.DateField()
    updated_at = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        db_table = 'product'
