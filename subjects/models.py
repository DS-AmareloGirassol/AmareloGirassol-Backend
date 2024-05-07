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
        help_text = ('Código da Disciplina')
    )

    def __str__(self):
        return self.name