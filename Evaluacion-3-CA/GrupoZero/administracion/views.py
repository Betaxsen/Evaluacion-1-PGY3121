from django.shortcuts import redirect, render
from administracion.models import usuario
from core.models import obra
from administracion.forms import usuarioForm
from administracion.form_mod import obraForm

# Create your views here.




def form_agregar(request):
    datos={
        'form':obraForm
    }

    if request.method == 'POST':
        formulario = obraForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"


    return render(request,'core/administracion/form_agregar.html',datos) 

def form_modificar(request,id):
    obran = obra.objects.get(idObra = id)
    
    datos = {
        'form':obraForm(instance=obran)
    }

    if request.method == "POST":
        formulario = obraForm(data=request.POST,instance=obran)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"
    return render(request,'core/administracion/form_modificar.html',datos) 


def form_del_obra(request,id):
    vehiculo = obra.objects.get(idObra = id)
    
    vehiculo.delete()

    return redirect(to="administracion")

def administracion(request):
    obras = obra.objects.all()
    datos={
        "obras":obras
    }
   
    return render(request, 'core/administracion.html',datos)



def sesionadministracion(request,):
    usuarios= usuario.objects.all()
    datos={
        'usuarios':usuarios #(instance=usuarion)
    }
  
    return render(request, 'core/sesionadministracion.html',datos)

