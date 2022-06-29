from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Carrito
from .serializers import CarritoSerializer
@csrf_exempt
@api_view(['GET','POST'])
def lista_carritos(request):
    """
    Lista todos los productos
    """
    if request.method== 'GET':
        carrito = Carrito.objects.all()
        serializer =CarritoSerializer(carrito, many=True)
        return  Response(serializer.data)
    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer = CarritoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def detalle_carrito(request, id):
    """
    Get, update, o delete de un producto en particular
    """
    try:
        carrito = Carrito.objects.get(idProducto=id)
    except Carrito.DoesNoExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CarritoSerializer(carrito, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        carrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)