from django.urls import path
from core.views import home, elemento, contacto, nosotros
from administracion.views import pantallalogin,sesionadministracion, administracion,form_agregar,form_modificar,form_del_obra, iniciosesion

urlpatterns = [
    path('',home,name="home"),
    path('elemento/<id>',elemento,name="elemento"),
    path('sesionadministracion',sesionadministracion,name="sesionadministracion"),
    path('administracion',administracion,name="administracion"),
    path('form-agregar', form_agregar,name="form_agregar"),
    path('form-modificar/<id>',form_modificar,name="form_modificar"),
    path('form-eliminar/<id>',form_del_obra,name="form_del_obra"),
    path('contacto',contacto,name="contacto"),
    path('nosotros',nosotros,name="nosotros"),
    path('pantallalogin',pantallalogin,name="pantallalogin"),
    path('inicio-sesion',iniciosesion,name="iniciosesion"),
     
]
