
from django.db import models

# Create your models here.
class usuario (models.Model):
     usuario = models.CharField(primary_key=True,max_length=50, verbose_name="usuario")
     contraseña = models.CharField(max_length=50,verbose_name="contraseña")
     def __str__(self):
         return self.usuario



