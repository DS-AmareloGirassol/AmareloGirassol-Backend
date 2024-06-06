from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length = 50,
        blank = False,
        null = False,
        help_text = ('Nome do Post')
    )

    description = models.CharField(
        max_length = 500,
        blank = False,
        null = False,
        help_text = ('Descricao do Post')
    )

    link = models.URLField(
        max_length = 100,
        blank = False,
        null = False,
        help_text = ('Link do Post')
    )
    
    def __str__(self):
        return self.name