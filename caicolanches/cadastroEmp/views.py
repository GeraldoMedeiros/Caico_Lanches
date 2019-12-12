from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView

from .forms import InsereEstabelecimentoForm
from .models import Estabelecimento


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "cadastroEmp/index.html"


class EstabelecimentoListView(ListView):
    template_name = "cadastroEmp/lista.html"
    model = Estabelecimento
    context_object_name = "estabelecimentos"


class EstabelecimentoCreateView(CreateView):
    template_name = "cadastroEmp/cria.html"
    model = Estabelecimento
    form_class = InsereEstabelecimentoForm
    success_url = reverse_lazy("cadastroEmp:lista_estabelecimentos")


class EstabelecimentoUpdateView(UpdateView):
    template_name = "cadastroEmp/atualiza.html"
    model = Estabelecimento
    fields = '__all__'
    context_object_name = 'estabelecimento'
    success_url = reverse_lazy("cadastroEmp:lista_estabelecimentos")


class EstabelecimentoDeleteView(DeleteView):
    template_name = "cadastroEmp/exclui.html"
    model = Estabelecimento
    context_object_name = 'estabelecimento'
    success_url = reverse_lazy("cadastroEmp:lista_estabelecimentos")
