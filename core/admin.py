from django.contrib import admin

from core.models import Autor, Categoria, Compra, ItensCompra


admin.site.register(Autor)
admin.site.register(Categoria)


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inline = (ItensInline,)
