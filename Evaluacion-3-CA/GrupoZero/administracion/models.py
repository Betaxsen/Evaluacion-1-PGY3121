
from django.db import models

# Create your models here.
class usuario (models.Model):
     nombre = models.CharField(primary_key=True,max_length=50, verbose_name="nombre",default="grupozero")
     contrasena = models.CharField(max_length=50,verbose_name="contrasena",default="grupozero")
     def __str__(self):
         return self.nombre



