from django.db import models

class Pessoa(models.Model):
    nome = models.TextField(null=False)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    telefone = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.nome