# Django
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# Settings check

# assert settings.PAYCOM_SETTINGS.get('SECRET_KEY') != None
from config.config.payme_settings import PAYCOM_SETTINGS

# User model
user_model = get_user_model()


class Command(BaseCommand):
    help = 'Create User for payments'
    username = 'Paycom'
    password = PAYCOM_SETTINGS['SECRET_KEY']
    username_key = user_model.USERNAME_FIELD

    def handle(self, *args, **options):
        try:
            user, _ = user_model.objects.update_or_create(**{self.username_key: self.username})
            user.set_password(self.password)
            user.save()
            self.stdout.write(self.style.SUCCESS('Success created user'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
