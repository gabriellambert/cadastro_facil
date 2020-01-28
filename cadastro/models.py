from django.db import models

SEXO_CHOICES = [
    ('F', 'Feminino'),
    ('M', 'Masculino'),
    ('O', 'Outros'),
]

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    email = models.EmailField()
    idade = models.IntegerField()

    def __str__(self):
        return self.nome
