from django.urls import path
from administracion.views import sesionadministracion

urlpatterns = [
 
    #path('administracion',administracion,name="administracion"),
    path('sesionadministracion',sesionadministracion,name="sesionadministracion"),
     
]
