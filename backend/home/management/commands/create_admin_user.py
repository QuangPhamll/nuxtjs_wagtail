from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, **options):
        user_model = get_user_model()

        if not user_model.objects.filter(username='admin').exists():
            user = user_model.objects.create_user('admin', password='changeme')
            user.is_superuser = True
            user.is_staff = True
            user.save()
