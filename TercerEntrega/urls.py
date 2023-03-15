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
from Aplicacion.views import index, mostrar_profesores, mostrar_curso, mostrar_alumnos, agregar_alumno, agregar_curso, agregar_profesor, buscar_curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("profesores/", mostrar_profesores, name="profesores"),
    path("admin-cursos/", mostrar_curso, name="admin-cursos"),
    path("alumnos/", mostrar_alumnos, name="alumnos"),
    path("profesores/agregar", agregar_profesor, name="agregar-profesor"),
    path("admin-cursos/agregar", agregar_curso, name="agregar-curso"),
    path("alumnos/agregar", agregar_alumno, name="agregar-alumno"),
    path("admin-cursos/buscar_curso", buscar_curso, name="buscar-curso"),
]
