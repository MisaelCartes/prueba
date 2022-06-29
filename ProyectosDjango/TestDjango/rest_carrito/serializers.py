from rest_framework import serializers
from core.models import Carrito
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields =['idProducto','nombreProducto','imagen','precio','cantidad']