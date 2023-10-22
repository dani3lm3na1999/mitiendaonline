from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(null=True, verbose_name="Descripción", max_length=200)
    existencias = models.IntegerField(null=False, verbose_name="Existencias")
    precio = models.DecimalField(null=False, verbose_name="Precio", decimal_places=2, max_digits=18)