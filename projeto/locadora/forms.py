from dataclasses import fields
from pyexpat import model
from unittest import mock
from django import forms

from .models import Veiculo
from .models import Motorista
from .models import Controle

class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = ('placa' , 'marca' , 'veiculo' , 'troca_oleo')

class MotoristaForm(forms.ModelForm):

    class Meta:
        model = Motorista
        fields = ('nome' , 'fone' , 'cnh')

class ControleForm(forms.ModelForm):

    class Meta:
        model = Controle
        # fields = ('veiculo' , 'motorista' , 'data_saida' , 'hora_saida' , 'km_saida' , 'destino' , 'data_retorno' , 'hora_retorno' , 'km_retorno' , 'km_percorrido')
        fields = '__all__'