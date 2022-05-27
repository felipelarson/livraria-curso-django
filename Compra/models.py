from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

from Livro.models import Livro


class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, "Carrinho"
        REALIZADO = 2, "Realizado"
        PAGO = 3, "Pago"
        ENTREGUE = 4, "Entregue"

    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="compras"
    )
    status = models.IntegerField(
        choices=StatusCompra.choices, default=StatusCompra.CARRINHO
    )

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F("quantidade") * F("livro__preco"))
        )
        return queryset["total"]


class ItensCompra(models.Model):
    compra = models.ForeignKey(
        Compra, on_delete=models.CASCADE, related_name="itens"
    )
    livro = models.ForeignKey(
        Livro, on_delete=models.PROTECT, related_name="+"
    )
    quantidade = models.IntegerField()
