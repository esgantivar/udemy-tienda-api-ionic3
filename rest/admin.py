from django.contrib import admin

# Register your models here.
from rest.models import Linea, Producto, Orden, DetalleOrden


class OrdenAdmin(admin.ModelAdmin):
    class DetailInline(admin.TabularInline):
        model = DetalleOrden
        extra = 0

    inlines = [DetailInline]


admin.site.register(Linea)
admin.site.register(Producto)
admin.site.register(Orden, OrdenAdmin)
