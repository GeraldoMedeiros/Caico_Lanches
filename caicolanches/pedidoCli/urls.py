from django.urls import path
from pedidoCli.views import IndexTemplateView, ClienteListView, ClienteUpdateView, ClienteCreateView, ClienteDeleteView
from pedidoCli.views import ProdutoCreateView

from . import views

app_name = 'pedidoCli'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),

    path('cliente/cadastrar', ClienteCreateView.as_view(), name="cadastra_cliente"),

    path('clientes/', ClienteListView.as_view(), name="lista_clientes"),

    path('cliente/<pk>', ClienteUpdateView.as_view(), name="atualiza_cliente"),

    path('cliente/excluir/<pk>', ClienteDeleteView.as_view(), name="deleta_cliente"),

    path('produto/cadastrar', ProdutoCreateView.as_view(), name="cadastra_produto"),


]
