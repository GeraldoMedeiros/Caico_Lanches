from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import Cliente, Produto
from .forms import InsereClienteForm, InsereProdutoForm


class IndexTemplateView(TemplateView):
    template_name = "pedidoCli/index.html"


class ClienteListView(ListView):
    template_name = "pedidoCli/lista.html"
    model = Cliente
    context_object_name = 'clientes'


class ClienteCreateView(CreateView):
    template_name = "pedidoCli/cria.html"
    model = Cliente
    form_class = InsereClienteForm
    success_url = reverse_lazy("pedidoCli:lista_clientes")


class ClienteUpdateView(UpdateView):
    template_name = "pedidoCli/atualiza.html"
    model = Cliente
    fields = '__all__'
    context_object_name = 'cliente'
    success_url = reverse_lazy("pedidoCli:lista_clientes")


class ClienteDeleteView(DeleteView):
    template_name = "pedidoCli/exclui.html"
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy("pedidoCli:lista_clientes")


class ProdutoCreateView(CreateView):
    template_name = "pedidoCli/criapro.html"
    model = Produto
    form_class = InsereProdutoForm
    success_url = reverse_lazy("pedidoCli:lista_produtos")
