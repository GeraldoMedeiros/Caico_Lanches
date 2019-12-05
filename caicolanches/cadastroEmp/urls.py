from django.urls import path
from cadastroEmp.views import IndexTemplateView, EstabelecimentoListView, EstabelecimentoUpdateView, EstabelecimentoCreateView, \
    EstabelecimentoDeleteView

from . import views

app_name = 'cadastroEmp'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),

    path('estabelecimento/cadastrar', EstabelecimentoCreateView.as_view(), name="cadastra_estabelecimento"),

    path('estabelecimentos/', EstabelecimentoListView.as_view(), name="lista_estabelecimentos"),

    path('estabelecimento/<pk>', EstabelecimentoUpdateView.as_view(), name="atualiza_estabelecimento"),

    path('estabelecimento/excluir/<pk>', EstabelecimentoDeleteView.as_view(), name="deleta_estabelecimento"),
]