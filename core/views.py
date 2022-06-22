from django.shortcuts import render
from .models import Producto

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def catalogo(request):
    productos = Producto.objects.all()
    data ={
        'productos' : productos
    }
    return render(request,'core/catalogo.html',data)

def quienessomos(request):
    return render(request,'core/quienessomos.html')

def sing(request):
    return render(request,'core/sign.html')

def login(request):
    return render(request,'core/login.html')

def listadoproductos(request): 
    return render(request,'core/listadoproductos.html')

def agregarproductos(request):
    return render(request,'core/agregarproductos.html')