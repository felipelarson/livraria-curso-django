from django.contrib import admin

from core.models import Categoria, Compra, ItensCompra


admin.site.register(Categoria)


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inline = (ItensInline,)
