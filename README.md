# actividad_m7_l6.
Proyecto educativo - CRUD en Django

# 📚 Librería Infantil - CRUD con Django

Este proyecto consiste en una aplicación web desarrollada con Django que permite gestionar un catálogo de libros infantiles mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

---

## 🔄 ¿Cómo funciona el flujo completo de una operación CRUD?

El flujo CRUD en este proyecto sigue una estructura clara basada en el patrón de Django: **URL → Vista → Modelo → Template**.

### 1. Crear (Create)
- El usuario accede a la URL `/libros/crear/`.
- Se muestra un formulario (`formulario_libro.html`).
- Al enviar el formulario (POST), la vista recoge los datos.
- Se crea un nuevo registro en la base de datos usando el modelo `Libro`.
- Finalmente, se redirige al listado de libros.

### 2. Leer (Read)
- El usuario accede a `/libros/`.
- La vista consulta todos los libros con `Libro.objects.all()`.
- Los datos se envían al template `listar_libros.html`.
- El template muestra la lista de libros en pantalla.

### 3. Actualizar (Update)
- El usuario hace clic en “Editar” en un libro.
- Se accede a `/libros/editar/<id>/`.
- La vista obtiene el libro usando su ID.
- Se muestra el formulario con los datos actuales.
- Al enviar el formulario, se actualizan los datos en la base de datos.
- Se redirige nuevamente al listado.

### 4. Eliminar (Delete)
- El usuario hace clic en “Eliminar”.
- Se accede a `/libros/eliminar/<id>/`.
- Se muestra una página de confirmación.
- Al confirmar (POST), el libro se elimina de la base de datos.
- Se redirige al listado de libros.

---

## 🌐 ¿Qué aprendí sobre el enrutamiento y los parámetros dinámicos en URLs?

Durante el desarrollo del proyecto aprendí cómo funciona el enrutamiento en Django mediante el uso de archivos `urls.py`.

### Enrutamiento
- Las URLs permiten conectar las rutas del navegador con funciones en `views.py`.
- Por ejemplo:
  ```python
  path('libros/', views.listar_libros, name='listar_libros')