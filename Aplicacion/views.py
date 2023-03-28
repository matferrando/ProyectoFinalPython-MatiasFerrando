from django.shortcuts import render
from Aplicacion.models import Post, Alumno, Profesor
from Aplicacion.forms import PostForm, AlumnoForm, ProfesorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

def agregar_curso(request):
    curso_form = PostForm(request.POST)
    curso_form.save()
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render(request, "Aplicacion/admin_cursos.html", context)

def agregar_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    alumno_form.save()
    context = {
        "form": AlumnoForm(),
        "alumnos": Alumno.objects.all(),
    }
    return render(request, "Aplicacion/alumnos.html", context)

def agregar_profesor(request):
    profesor_form = ProfesorForm(request.POST)
    profesor_form.save()
    context = {
        "form": ProfesorForm(),
        "profesores": Profesor.objects.all(),
    }
    return render(request, "Aplicacion/profesores.html", context)

def buscar_curso(request):
    criterio = request.GET.get("criterio")
    context = {
        "posts": Post.objects.filter(nombre_del_curso__icontains=criterio).all(),
    }
    return render(request, "Aplicacion/admin_cursos.html", context)


class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"