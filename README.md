Задание 1
 - к модели продуктов добавлено логическое поле publish_status "Статус публикации". Значение по умолчанию False;
 - создана группа Moderators, ей назначены права can_unpublish_product и удаление продуктов;
 - созданы кастомные команды для создания группы Модераторов, для создания пользователя модератора, для включения пользователя модератора в группу модераторов;
   - настроена проверка в контроллере на наличие права при попытке отменить публикацию:
               `if not request.user.has_perm('catalog.can_unpublish_product'):
               return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.");
   ` - настроена проверка в контроллере при попытке удалить продукт:
   `         if self.get_object().owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
               return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")
   `Задание 2
 - добавлено поле владельца (owner) к модели продукта, связано с полем пользователя в модели Users через ForeignKey
 owner = models.ForeignKey(User, verbose_name="Владелец продукта",  on_delete=models.PROTECT, related_name='products');
- в контроллере CBV создания продукта настроено автоматическое заполнение поля владельца значением текущего пользователя

 `   def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form);
` - настроена проверка в контроллере, чтобы только владелец и модератор могли удалять продукт и только владелец мог редактировать редактировать продукт


     def post(self, request, *args, **kwargs):
        if self.get_object().owner != request.user:
            return HttpResponseForbidden("У вас нет прав для редактирования этого продукта.")
        self.get_object().save()
        return redirect('catalog:products_list_f')

    def post(self, request, *args, **kwargs):
        if self.get_object().owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")
        self.get_object().delete()
        return redirect('catalog:products_list_f');
- в шаблоне настроена проверка, чтобы кнопки редактирования удаления отображались только для владельца продукта
                     
       {% if prod.owner == user %}
       <a href="{% url 'catalog:product_update' prod.pk %}" class="btn btn-sm btn-secondary ml-3">Редактировать</a>
       <a href="{% url 'catalog:product_delete' prod.pk %}" class="btn btn-sm btn-danger ml-1">Удалить</a>
       {% endif %}
                   

 