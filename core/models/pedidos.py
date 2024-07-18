from django.db import models
from .clientes import Cliente
from .pecas import Peca

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    peca = models.ManyToManyField(Peca)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dia = models.DateField()

    def __str__(self):
        return f"{self.cliente.pessoa.nome} - {self.dia} - {self.valor}"