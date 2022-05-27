from django.contrib import admin

from Compra.models import Compra, ItensCompra


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inline = (ItensInline,)
