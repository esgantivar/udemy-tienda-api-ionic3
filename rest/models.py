from django.contrib.auth.models import User
from django.db import models
from api.settings import SITE_URL


# Create your models here.


class Linea(models.Model):
    linea = models.CharField(verbose_name='Linea', max_length=100)
    icono = models.CharField(verbose_name='icono', max_length=20)

    class Meta:
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id} - {self.linea}'


class Producto(models.Model):
    codigo = models.CharField(max_length=15)
    producto = models.CharField(max_length=70)
    linea = models.CharField(max_length=50)
    fk_linea = models.ForeignKey(to=Linea, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_compra = models.FloatField()
    imagen = models.FileField(verbose_name='Imagen', upload_to='productos', null=True, blank=True)

    class Meta:
        verbose_name = 'Productos'
        verbose_name_plural = 'Productos'
        ordering = ('id',)

    def __str__(self):
        return f'{self.codigo} - {self.producto}'

    @property
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'producto': self.producto,
            'linea': self.linea,
            'proveedor': self.proveedor,
            'descripcion': self.descripcion,
            'precio_compra': self.precio_compra,
            'imagen': f'{SITE_URL}{self.imagen.url}' if self.imagen else ''
        }


class Orden(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    creado_en = models.DateField(verbose_name='Creado en', auto_now_add=True)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
        ordering = ('-creado_en',)

    def __str__(self):
        return f'{self.id} - {self.user.username} - {self.creado_en}'

    @property
    def to_dict(self):
        products = []
        for p in Producto.objects.filter(id__in=DetalleOrden.objects.filter(orden=self).values_list('id', flat=True)):
            products.append(p.to_dict)

        return {
            'id': self.id,
            'creado_en': self.creado_en,
            'detalle': products
        }


class DetalleOrden(models.Model):
    orden = models.ForeignKey(to=Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.producto}'
