from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    nombre_del_curso = models.CharField(max_length=30)
    descripcion_del_curso = models.CharField(max_length=80)
    numero_del_curso = models.CharField(max_length=15)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher")
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    @property 
    def image_url(self):
        return self.image.url if self.image else ''

    def __str__(self):
        return f"{self.numero_del_curso} - {self.nombre_del_curso}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    especialidad = models.CharField(max_length=40)

class Profesor(models.Model):
    nombre_del_profesor = models.CharField(max_length=20)
    apellido_del_profesor = models.CharField(max_length=20)
    numero_de_profesor = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.numero_de_profesor} - {self.nombre_del_profesor} {self.apellido_del_profesor}"
    
class Alumno(models.Model):
    nombre_del_alumno = models.CharField(max_length=20)
    apellido_del_alumno = models.CharField(max_length=20)
    numero_de_alumno = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.numero_de_alumno} - {self.nombre_del_alumno} {self.apellido_del_alumno}"