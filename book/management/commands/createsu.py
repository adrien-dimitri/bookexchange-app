from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='superbookadmin').exists():
            User.objects.create_superuser(
                username='superbookadmin',
                password='superbookadminpass'
            )
        print('Superuser has been created.')