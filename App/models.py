from sqlite3 import Cursor
from django.db import models
from .choices import sexos

# Create your models here.
class Estudiantes (models.Model):
    id_estudiante=models.IntegerField(primary_key=True)
    ci=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField()
    correo=models.EmailField()
    sexo=models.CharField(max_length=1,choices=sexos, default='M', )

    def nombre_completo (self):
        return "{} {}".format(self.nombre,self.apellido)

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Profesores (models.Model):
    id_profesor=models.IntegerField(primary_key=True)
    ci=models.CharField(max_length=10)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField()
    correo=models.EmailField()

class Cursos (models.Model):
    id_curso=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    credito=models.IntegerField()
    horario=models.CharField(max_length=100)
    id_profesor=models.ForeignKey(Profesores,on_delete=models.RESTRICT)

class Inscripcion (models.Model):
    id_inscripcion=models.IntegerField(primary_key=True)
    id_curso=models.ForeignKey(Cursos,on_delete=models.RESTRICT)
    id_estudiante=models.ForeignKey(Estudiantes,on_delete=models.RESTRICT)