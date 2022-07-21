from django.db import models

# Create your models here.

class usuario(models.Model):
    soied = models.CharField(max_length=8)
    nombre= models.CharField(max_length=50)
    direccion = models.CharField(max_length=150,default="Mexico")

