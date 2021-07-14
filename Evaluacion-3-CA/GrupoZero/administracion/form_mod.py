from django import forms
from django.db.models import fields
from django.forms import ModelForm
from core.models import  obra


class obraForm(ModelForm):
    class Meta:
        model = obra
        fields = ['idObra', 'detalle','valor','categorias','artista']

 