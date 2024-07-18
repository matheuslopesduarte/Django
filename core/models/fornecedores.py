from django.db import models
from .pessoas import Pessoa

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=14, null=False)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.PROTECT)

    def __str__(self):
        return self.pessoa.nome