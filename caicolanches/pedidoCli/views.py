from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
# Create your views here.

<<<<<<< HEAD

class IndexTemplateView(TemplateView):
    template_name = "pedidoCli/index.html"
=======
def index(request):
    return HttpResponse("Página do cliente em desenvolvimento!")
>>>>>>> 52cee33bf69c077b99494297b713d94d4d86fe87


# class ReceiverForm(forms.ModelForm):
#    phone_number = forms.RegexField(regex=r'\d{10,11}$', error_message = ("Entre com um número no formato: 'xx987654321'"))
