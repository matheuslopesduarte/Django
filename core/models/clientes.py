from django.db import models
from .pessoas import Pessoa

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, null=False) 
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome
