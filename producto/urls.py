from django.urls import path

from producto import views

urlpatterns =[
    path('', views.hello_world, name='inicio'),
    path('productos/', views.productos_list, name='productos'),
    path('productos/editar/<int:id>', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('lista_productos/', views.ListaProductos.as_view(),name="lista_productos"),
]