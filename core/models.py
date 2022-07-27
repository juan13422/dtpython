from django.db import models

# Create your models here.

class usuario(models.Model):
    soied = models.CharField(max_length=8)
    nombre= models.CharField(max_length=50)
    direccion = models.CharField(max_length=150,default="Mexico")

class ejercicios(models.Model):
    id_ejercicio = models.CharField(max_length=12)
    descripcion= models.CharField(max_length=150,default="Descripcion")
    do = models.CharField(max_length=12,default="do")
    detalle = models.CharField(max_length=150,default="Detalle")
    estatus = models.CharField(max_length=1,default="1")

