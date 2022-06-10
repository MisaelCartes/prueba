from django.db import models

# Create your models here.

#Modelo para categoria

class Carrito(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id de Producto')
    nombreProducto = models.CharField(max_length=50,verbose_name="Nombre de Producto")
    precio = models.IntegerField(verbose_name="Precio")
    cantidad = models.IntegerField(verbose_name="Cantidad")

    def __str__(self):
        return self.nombreProducto


