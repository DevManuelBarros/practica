from django.contrib import admin
from .models import Producto, Categoria


def publicar(modeladmin, request, queryset):
    queryset.update(estado='Publicado')

class ProductoAdmin(admin.ModelAdmin):
    fields = ['categoria', 'fecha_publicacion', 'producto', 'ruta_imagen', 'estado']
    list_display = ['producto', 'fecha_publicacion', 'ruta_imagen', 'tipo_de_producto']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion')
    actions = [publicar]

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)