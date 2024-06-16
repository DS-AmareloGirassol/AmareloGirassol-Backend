from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from .managers import PersonManager


class Person(AbstractUser):
    objects = PersonManager()
    
    name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True,
        null=False
    )

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.name} [{self.email}]'