from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    # help = 'Добавление группы Модераторы'

    def handle(self, *args, **kwargs):
        moderators_group = Group.objects.create(name='Moderators')
