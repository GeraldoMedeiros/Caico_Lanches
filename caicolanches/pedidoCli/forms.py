from .models import Cliente, Produto
from django import forms
#from models import *


class InsereClienteForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Cliente
        ###password = forms.CharField(widget=forms.PasswordInput)

        # Campos que estarão no form
        fields = [
            'nome',
            'cpf',
            'nascimento',
            'fone',
            'login',
            'password',
        ]
class InsereProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto

        fields = [
            'nome',
            'descricao',
            'preco',
        ]
