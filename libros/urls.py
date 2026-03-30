from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]

#ejemplo para agregar url: 
#path('info/', views.info)