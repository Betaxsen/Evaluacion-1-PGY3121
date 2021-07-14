from django.shortcuts import render
from core.models import obra

# Create your views here.

def home(request):
    obras = obra.objects.all()
    datos = {
        "obras":obras
    }
    return render(request, 'core/principal.html',datos)

def elemento(request,id): 
    obras = obra.objects.get(idObra = id)
    datos = {
        "obras":obras
    } 
    return render(request, 'core/objetos/elemento.html', datos)


def nosotros(request):
  
    return render(request, 'core/otros/Nosotros.html')
    

def contacto(request):
   
    return render(request, 'core/otros/Contacto.html')

def sesionadministracion(request):

    return render(request, 'core/sesionadministracion.html')


