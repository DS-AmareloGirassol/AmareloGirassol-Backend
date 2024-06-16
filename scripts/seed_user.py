#!/usr/local/bin/python

from persons.models import Person

# Usuários

Person.objects.create(
    name="João da Silva",
    email='joao@aluno.br',
    password='joao',
)

Person.objects.create(
    name="José Santos",
    email='jose@aluno.br',
    password='jose',
)
