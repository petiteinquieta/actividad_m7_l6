from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro


def inicio(request):
    total_libros = Libro.objects.count()
    return render(request, 'libros/inicio.html', {'total_libros': total_libros})


def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        anio_publicacion = request.POST.get('anio_publicacion')

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            anio_publicacion=anio_publicacion
        )
        return redirect('listar_libros')

    return render(request, 'libros/formulario_libro.html')


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.titulo = request.POST.get('titulo')
        libro.autor = request.POST.get('autor')
        libro.anio_publicacion = request.POST.get('anio_publicacion')
        libro.save()
        return redirect('listar_libros')

    return render(request, 'libros/formulario_libro.html', {'libro': libro})


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')

    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})