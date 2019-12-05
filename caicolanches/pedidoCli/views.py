from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Página do cliente em desenvolvimento!")


#class ReceiverForm(forms.ModelForm):
#    phone_number = forms.RegexField(regex=r'\d{10,11}$', error_message = ("Entre com um número no formato: 'xx987654321'"))
