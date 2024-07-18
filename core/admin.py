from django.contrib import admin

from core.models import Pessoa, Cliente, Fornecedor, Peca, Pedido

admin.site.register(Pessoa)
admin.site.register(Cliente)
admin.site.register(Fornecedor)
admin.site.register(Peca)
admin.site.register(Pedido)