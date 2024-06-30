#!/usr/local/bin/python

from persons.models import Person

# Usuários

Person.objects.create(
    name="João da Silva",
    email='joao@aluno.br',
    password='joao',
    description='oiwiooidwqo dhowhowhd',
    semester_being_attended = 5
)

Person.objects.create(
    name="José Santos",
    email='jose@aluno.br',
    password='jose',
    description='oiwiooidwqo dhowhowhd',
    semester_being_attended = 7
)
