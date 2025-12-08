from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок", null=True)
    content = models.TextField()
    prev_image = models.ImageField(upload_to='images/', verbose_name="Изображение", null=True)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    publication_flag = models.BooleanField(verbose_name="Признак публикации", null=True, default=False)
    number_of_views = models.IntegerField(verbose_name="Количество просмотров", null=False, default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ['title']
        db_table = 'blog_records'
