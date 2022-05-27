from django.contrib import admin

from core.models import Autor, Categoria, Compra, ItensCompra, Livro


admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Livro)


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inline = (ItensInline,)
