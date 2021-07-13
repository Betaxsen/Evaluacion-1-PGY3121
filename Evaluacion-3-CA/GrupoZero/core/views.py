from django.shortcuts import render
from core.models import obra

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def principal(request):
    obras = obra.objects.all()
    buscar = ""
    texto = ""
    datos = {
        "obras":obras,
        "buscar":buscar,
        "texto":texto
    }
    return render(request, 'core/principal.html',datos)


def elemento(request,id): 
    obras = obra.objects.get(idObra = id)
    datos = {
        "obras":obras
    } 
    return render(request, 'core/objetos/elemento.html', datos)
