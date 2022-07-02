from django.shortcuts import redirect, render
from .models import Producto
from .forms import CustomUserForm, ProductoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

#rets framework

from rest_framework import viewsets
from .serializers import ProductoSertializer


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

@login_required
def listadoproductos(request): 
    return render(request,'core/listadoproductos.html')


@permission_required('core.add_producto')
@login_required
def agregarproductos(request):
    data = {
        'form':ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"
        data['form'] = formulario        

    return render(request,'core/agregarproductos.html',data)

@login_required
def modificar_productos(request,id):
    producto = Producto.objects.get(id=id)
    data ={
        'form':ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamente"
        data['form'] = formulario

    return render(request,'core/modificar_productos.html',data)

@login_required
def eliminar_productos(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    
    return redirect(to="listadoproductos")

@login_required
def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    return render(request, "registration/registrar.html",data)













class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSertializer