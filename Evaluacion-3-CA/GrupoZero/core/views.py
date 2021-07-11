from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'core/home.html')

def principal(request):
    contexto = {"nombre":"bulbasaur"}
    return render(request, 'core/principal.html',contexto)

def  elemento(request):
    return render(request, 'core/objetos/ejemplo1.html')
