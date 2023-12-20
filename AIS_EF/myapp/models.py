from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    fecha_compra = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=1)