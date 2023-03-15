from django.shortcuts import render
from Aplicacion.models import Post, Alumno, Profesor
from Aplicacion.forms import PostForm, AlumnoForm, ProfesorForm

def index(request):
    return render(request, "Aplicacion/index.html")

def mostrar_profesores(request):
    context = {
        "form": ProfesorForm(), 
        "profesores": Profesor.objects.all(),
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
        "form": AlumnoForm(), 
        "alumnos": Alumno.objects.all(),
    }

    return render(request, "Aplicacion/alumnos.html", context)