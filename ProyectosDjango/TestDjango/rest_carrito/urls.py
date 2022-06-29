from django.urls import path
from rest_carrito.views import lista_carritos,detalle_carrito

urlpatterns =[
    path('lista_carritos',lista_carritos,name="lista_carritos"),
    path('detalle_carrito/<id>', detalle_carrito, name="detalle_carrito"),
]