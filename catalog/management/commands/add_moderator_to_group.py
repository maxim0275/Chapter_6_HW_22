from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from users_app.models import User


class Command(BaseCommand):
    # help = 'Добавление пользователя модератора в группу Модераторы'

    def handle(self, *args, **kwargs):
        moderators_group = Group.objects.get(name='Moderators')
        # Получаем пользователя
        user = User.objects.get(email='moderator@email.com')

        # Добавляем пользователя в группу «Редакторы»
        user.groups.add(moderators_group)