from django.shortcuts import render
from Aplicacion.models import Post
from Aplicacion.forms import PostForm

# from django.http import HttpResponse

# def saludo (request):
#     return HttpResponse("Hola Django - Coder")

# def saludo_a (request, nombre):
#     return HttpResponse(f"Hola Como estas {nombre.capitalize()}")

# def mostrar_mi_template(request):
#     context = {
#         "nombre": "Matias",
#         "apellido": "Ferrando"
#     }

#     return render(request, "Aplicacion/index.html", context)

def index(request):
    return render(request, "Aplicacion/index.html")

def mostrar_profesores(request):
    context = {
        "form": PostForm(), 
        "posts": Post.objects.all(),
    }

    return render(request, "Aplicacion/profesores.html", context)

def mostrar_curso(request):
    context = {
        "form": PostForm(), 
        "posts": Post.objects.all(),
    }

    return render(request, "Aplicacion/admin_cursos.html", context)

def mostrar_alumnos(request):
    context = {
        "form": PostForm(), 
        "posts": Post.objects.all(),
    }

    return render(request, "Aplicacion/alumnos.html", context)