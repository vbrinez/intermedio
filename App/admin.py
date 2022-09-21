from atexit import register
import site
from django.contrib import admin
from .models import Estudiantes,Profesores,Cursos,Inscripcion

# Register your models here.
admin.site.register(Estudiantes),
admin.site.register(Profesores),
admin.site.register(Cursos),
admin.site.register(Inscripcion),