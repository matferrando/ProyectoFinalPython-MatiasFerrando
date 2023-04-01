from django.shortcuts import render
from Aplicacion.models import Post, Alumno, Profesor, Profile
from Aplicacion.forms import PostForm, AlumnoForm, ProfesorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "Aplicacion/index.html")

def about(request):
    return render(request, "Aplicacion/about.html")

def mensajes(request):
    return render(request, "Aplicacion/mensajes.html")

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

class PostMineList(LoginRequiredMixin, PostList):
    def get_queryset(self):
        return  Post.objects.filter(publisher=self.request.user.id).all()
 
class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

class PermisoMod(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()

class PostUpdate(LoginRequiredMixin, PermisoMod, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = "__all__"


class PostDelete(LoginRequiredMixin, PermisoMod,DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = "__all__"

class PostSearch(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Post.objects.filter(nombre_del_curso__icontains=criterio).all()
        return result
    

class Login(LoginView):
    next_page = reverse_lazy("index")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("index")

class Logout(LogoutView):
    template_name = "registration/logout.html"

class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ["avatar", "especialidad"]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProfileUpdate(UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = ["avatar", "especialidad"]

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()
    