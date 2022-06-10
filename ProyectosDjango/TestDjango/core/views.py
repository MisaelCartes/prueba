from django.shortcuts import render
from .models import Carrito
# Create your views here.

def home(request):
    return render(request,'core/home.html')

def donaciones(request):
    return render(request,'core/donaciones.html')

def insumos(request):
    return render(request,'core/insumos.html')

def maceteros(request):
        
    Carritos= Carrito.objects.all()

    datos = {
        'Carritos': Carritos
    }
    
    return render(request,'core/maceteros.html', datos)

def paginalogin(request):
    return render(request,'core/paginalogin.html')

def perfil(request):
    
    Carritos= Carrito.objects.all()

    datos = {
        'Carritos': Carritos
    }
    return render(request,'core/perfil.html', datos)

def registro(request):
    return render(request,'core/registro.html')