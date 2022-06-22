from django.urls import path
from .views import index,catalogo,quienessomos,login,sing,listadoproductos,agregarproductos

urlpatterns = [
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('quienessomos/',quienessomos, name="quienesomos"),
    path('login/', login, name="login"),
    path('sign/', sing, name="sign"),
    path('listaproductos/', listadoproductos, name="listaproductos"),
    path('agregarproductos/',agregarproductos, name="agregarproductos")
]