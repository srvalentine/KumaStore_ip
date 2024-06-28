from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.cargarInicio),
    path('inicio', views.cargarInicio),
    path('login', views.cargarSesion),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('agregarProductoForm', views.agregarProducto),
    path('eliminarProducto/<sku>', views.eliminarProducto),
    path('editarProducto/<sku>', views.cargarEditarProductos),
    path('editarProductoForm', views.editarProductoForm),
    path('registrar', views.cargarAgregarUsuario, name='registrar'),
    path('agregarUsuarioForm', views.agregarUsuario),
    path('mapa', views.cargarMapa),
    path('api/modelos/', views.transformarDatos, name='transformarDatos')
]