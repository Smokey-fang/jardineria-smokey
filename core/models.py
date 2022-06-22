from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion =models.TextField()
    marca = models.ForeignKey(Marca, on_delete=CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.nombre