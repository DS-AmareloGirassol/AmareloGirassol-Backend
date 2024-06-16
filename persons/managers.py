from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class PersonManager(BaseUserManager):
    def create(self, email, password = None, **extra_fields):
        try:
            if not email:
                raise ValueError(_('Email is required'))

            email = self.normalize_email(email)

            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()

            return user
        except Exception as error:
            raise Exception('Error Create User: ' + str(error))