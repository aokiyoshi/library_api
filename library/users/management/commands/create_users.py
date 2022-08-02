import email
from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from library.utils import make_random_string

class Command(BaseCommand):
    help = 'Create superuser and some test users'

    def handle(self, *args, **kwargs):
        user = get_user_model()
        if not user.objects.filter(username='admin'):
            get_user_model().objects.create_superuser(
                    username='admin',
                    email='admin@localhost', 
                    password='admin111')

        for _ in range(5):
            user_name = make_random_string(5)

            user.objects.create(
                username=user_name,
                email=f'{user_name}@somemail.com',
                password=make_password('user_name'),
            )
