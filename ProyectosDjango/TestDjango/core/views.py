from django.shortcuts import render,redirect
from .models import Carrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'core/home.html')

def donaciones(request):
    return render(request,'core/donaciones.html')

def insumos(request):
    return render(request,'core/insumos.html')

def maceteros(request):
        
    Carritos= Carrito.objects.all()
    
    return render(request,'core/maceteros.html',{'Carritos': Carritos})

def paginalogin(request):
    return render(request,'core/paginalogin.html')

def perfil(request):
    
    Carritos= Carrito.objects.all()

    datos = {
        'Carritos': Carritos
    }
    return render(request,'core/perfil.html', datos)

def registro(request):
    if request.method =='POST':
        form =UserCreationForm  (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            message.success(request,f'usuario{username}creado')
            return redirect('core/home.html')
        else:
            form=UserCreationForm()
        context = {'form'.form}
    return render (request,'core/registro.html' )