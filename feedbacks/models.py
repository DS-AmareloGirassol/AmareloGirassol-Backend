from django.db import models

from persons.models import Person
from subjects.models import  Subject


class Feedback(models.Model):
    metodologia = models.IntegerField(
        blank = False,
        null = False,
        default = 1
    )

    didatica = models.IntegerField(
        blank = False,
        null = False,
        default = 1
    )

    suporte_professor = models.IntegerField(
        blank = False,
        null = False,
        default = 1
    )

    monitoria = models.IntegerField(
        blank = False,
        null = False,
        default = 1
    )

    indice_recomendacao = models.IntegerField(
        blank = False,
        null = False,
        default = 1
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