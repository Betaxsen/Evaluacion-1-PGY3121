from django.urls import path
from core.views import home, principal, elemento
from administracion.views import sesionadministracion, administracion,form_agregar,form_modificar,form_del_obra, iniciosesion

urlpatterns = [
    path('',home,name="home"),
    path('principal',principal,name="principal"),
    path('elemento/<id>',elemento,name="elemento"),
    path('sesionadministracion',sesionadministracion,name="sesionadministracion"),
    path('administracion',administracion,name="administracion"),
    path('form-agregar', form_agregar,name="form_agregar"),
    path('form-modificar/<id>',form_modificar,name="form_modificar"),
    path('form-eliminar/<id>',form_del_obra,name="form_del_obra"),
    path('iniciosesion/<id>',iniciosesion,name="iniciosesion"),
     
]
