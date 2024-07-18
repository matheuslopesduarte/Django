from django.db import models
from .fornecedores import Fornecedor

class Peca(models.Model):
    nome = models.TextField(null=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nome