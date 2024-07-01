from django.db import models

from persons.models import Person
from subjects.models import  Subject


class Feedback(models.Model):
    metodologia = models.IntegerField(
        blank = False,
        null = False,
        default = 3
    )

    trabalho = models.IntegerField(
        blank = False,
        null = False,
        default = 3
    )

    provas = models.IntegerField(
        blank = False,
        null = False,
        default = 3
    )

    material = models.IntegerField(
        blank = False,
        null = False,
        default = 3
    )

    facilidade = models.IntegerField(
        blank = False,
        null = False,
        default = 3
    )

    user = models.ForeignKey(
        Person,
        blank = False,
        null = False,
        on_delete = models.PROTECT,
    )

    subject = models.ForeignKey(
        Subject,
        blank = False,
        null = False,
        on_delete = models.PROTECT,
    )