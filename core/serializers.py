from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)
from rest_framework import serializers

from core.models import Autor, Compra, Categoria, ItensCompra


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = (
            "livro",
            "quantidade",
            "total",
        )
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.livro.preco


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = SerializerMethodField()
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = (
            "id",
            "status",
            "usuario",
            "itens",
            "total",
        )

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("id", "livro", "quantidade")

    def validate(self, data):
        if data["quantidade"] > data["livro"].quantidade:
            raise serializers.ValidationError(
                {
                    "quantidade": "Quantidade solicitada não disponível em estoque."
                }
            )
        return data


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance
