from django.db import router
from django.urls import include, path
from .views import eliminar_productos, index,catalogo, modificar_productos,quienessomos,login, registro_usuario,sing,listadoproductos,agregarproductos
from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls.conf import include

from .views import ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('quienessomos/',quienessomos, name="quienesomos"),
    path('login/', login, name="login"),
    path('sign/', sing, name="sign"),
    path('listaproductos/', listadoproductos, name="listaproductos"),
    path('agregarproductos/',agregarproductos, name="agregarproductos"),
    path('modificar_producto/<id>/',modificar_productos, name='modificar_productos'),
    path('eliminar_productos/<id>/',eliminar_productos, name='eliminar_productos'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('api/', include(router.urls)),
]