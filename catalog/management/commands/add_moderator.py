from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    # help = 'Добавление пользователя модератора'

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='moderator@email.com'
        )
        user.set_password('123')
        user.save()
        self.stdout.write(self.style.SUCCESS(f'Создан пользователь {user.email}'))
