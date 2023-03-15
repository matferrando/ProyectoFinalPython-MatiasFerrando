from django.db import models

class Post(models.Model):
    nombre_del_curso = models.CharField(max_length=30)
    descripcion_del_curso = models.CharField(max_length=80)
    numero_del_curso = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.numero_del_curso} - {self.nombre_del_curso}"
    
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