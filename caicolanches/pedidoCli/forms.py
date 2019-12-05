from .models import Cliente
from django import forms


class InsereClienteForm(forms.ModelForm):

    class Meta:
        # Modelo base
        model = Cliente

        # Campos que estarão no form
        fields = [
            'nome',
            'cpf',
            'nascimento',
            'fone',
            'login',
            'password',
            'endereco',
        ]
