from django.db import models

# Create your models here.
class artista (models.Model):
     idartista = models.IntegerField(primary_key=True, verbose_name="Id Artista")
     nombreartista = models.CharField(max_length=50,verbose_name="Nombre Artista")
     def __str__(self):
         return self.nombreartista

class obra (models.Model):
     idObra = models.IntegerField(primary_key=True, verbose_name="Id Obra")
     detalle = models.CharField(max_length=50,verbose_name="Detalle")
     valor = models.CharField(max_length=50,verbose_name="Valor")
     categorias = models.CharField(max_length=50,verbose_name="Categoria")
     artista = models.ForeignKey(artista, on_delete= models.CASCADE)
     def __str__(self):
         return self.detalle