from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from subjects.models import Subject

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

    subjects = models.ManyToManyField(Subject, blank=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'{self.name} [{self.email}]'
    

    def add_all_subject_studied(self, subject_list):
        try:
            self.subjects.clear()
            
            for sub_id in subject_list:
                subject_studied = Subject.objects.get(pk = sub_id)

                self.subjects.add(subject_studied)
        except Exception as error:
            raise Exception(str(error))
        
    def get_all_subjects(self):
        return self.subjects.all()