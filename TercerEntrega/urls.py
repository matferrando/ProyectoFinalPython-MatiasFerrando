"""TercerEntrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicacion.views import index, mostrar_profesores, mostrar_curso, mostrar_alumnos, agregar_alumno, agregar_curso, agregar_profesor, buscar_curso, PostList, PostDetail, PostUpdate, PostDelete, PostCreate, PostSearch, Login, SignUp, Logout, PostMineList, ProfileCreate, ProfileUpdate, about, MensajeCreate, MensajeDelete, MensajeList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("profesores/", mostrar_profesores, name="profesores"),
    path("admin-cursos/", mostrar_curso, name="admin-cursos"),
    path("alumnos/", mostrar_alumnos, name="alumnos"),
    path("profesores/agregar", agregar_profesor, name="agregar-profesor"),
    path("admin-cursos/agregar", agregar_curso, name="agregar-curso"),
    path("alumnos/agregar", agregar_alumno, name="agregar-alumno"),
    path("admin-cursos/buscar_curso", buscar_curso, name="buscar-curso"),
    path("post/list", PostList.as_view(), name="post-list"),
    path("post/<pk>/detail", PostDetail.as_view(), name="post-detail"),
    path("post/<pk>/update", PostUpdate.as_view(), name="post-update"),
    path("post/<pk>/delete", PostDelete.as_view(), name="post-delete"),
    path("post/create", PostCreate.as_view(), name="post-create"),
    path("post/search", PostSearch.as_view(), name="post-search"),
    path("login/", Login.as_view(), name="login"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("logout/", Logout.as_view(), name="logout"),
    path("post/list/mine", PostMineList.as_view(), name="post-mine"),
    path("profile/create", ProfileCreate.as_view(), name="profile-create"),
    path("profile/<pk>/update", ProfileUpdate.as_view(), name="profile-update"),
    path("mensaje/list", MensajeList.as_view(), name="mensaje-list"),
    path("mensaje/create", MensajeCreate.as_view(), name="mensaje-create"),
    path("mensaje/<pk>/delete", MensajeDelete.as_view(), name="mensaje-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  