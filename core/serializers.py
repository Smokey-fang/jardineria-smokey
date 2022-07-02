from dataclasses import fields
from rest_framework import serializers
from .models import Producto

class ProductoSertializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ['nombre','precio','descripcion','marca','imagen']



