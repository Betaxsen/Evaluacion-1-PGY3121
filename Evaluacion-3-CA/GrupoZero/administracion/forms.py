
from django import forms
from django.db.models import fields
from django.forms import ModelForm
from administracion.models import  usuario


class usuarioForm(ModelForm):
    class Meta:
        model = usuario
        fields = ['usuario', 'contraseña']

 