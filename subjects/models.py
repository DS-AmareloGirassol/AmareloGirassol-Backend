from django.db import models

class Subject(models.Model):
    name = models.CharField(
        max_length = 40,
        blank = False,
        null = False,
        help_text = ('Nome da Matéria')
    )

    code = models.CharField(
        max_length = 10,
        blank = False,
        null = False,
        unique = True,
        help_text = ('Código da Disciplina')
    )

    workload = models.IntegerField(
        blank = False,
        null = False
    )

    default_semester = models.IntegerField(
        blank = False,
        null = False
    )

    def __str__(self):
        return self.name