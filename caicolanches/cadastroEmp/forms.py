from .models import Estabelecimento
from django import forms


class InsereEstabelecimentoForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Estabelecimento

        # Campos que estarão no form
        fields = [
            'nomeFrant',
            'social',
            'cnpj',
            'fone',
            'login',
            'password',
            'endereco',
            'responsavel'
        ]