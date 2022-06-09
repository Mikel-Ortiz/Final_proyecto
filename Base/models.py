from distutils.command.upload import upload
from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from statistics import median
from django.contrib.auth.models import User

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=200)
    descripción = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.nombre

class Linea_de_Investigacion(models.Model):
    linea_de_investigacion = models.CharField(max_length=200)
    descripción = models.CharField(max_length=200)
    responsable = models.CharField(max_length=200)

    def __str__(self):
        return self.linea_de_investigacion

class Eventos(models.Model):
    nombre = models.CharField(max_length=200)
    descripción = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="media/")
    fecha_subido = models.DateTimeField(default=timezone.now)

    readonly_fields = ('fecha_subido')

    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    asunto = models.CharField(max_length=250)
    mensaje = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre

