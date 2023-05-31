from django.urls import path
from projeto5 import views


urlpatterns = [
    path(
        'projeto05/clientes/carregar-dados',
        views.ClientesLoadData.as_view(),
        name='clientes-carregar-dados',
    ),
    path(
        'projeto05/pedidos/carregar-dados',
        views.PedidosLoadData.as_view(),
        name='pedidos-carregar-dados',
    ),
    path(
        'projeto05/vendedores/carregar-dados',
        views.VendedoresLoadData.as_view(),
        name='vendedores-carregar-dados',
    ),
    path(
        'projeto05/clientes',
        views.ClientesList.as_view(),
        name='clientes-list',
    ),
    path(
        'projeto05/pedidos/media',
        views.PedidosMediaValor.as_view(),
        name='pedidos-media',
    ),
    path(
        'projeto05/pedidos/media-por-cidade',
        views.PedidosMediaPorCidade.as_view(),
        name='pedidos-media-por-cidade',
    ),
    path(
        'projeto05/pedidos/media-por-cidade-incluindo-cidades-sem-pedido',
        views.PedidosMediaPorCidadeIncluindoSemPedidos.as_view(),
        name='pedidos-media-por-cidade-incluindo-zero',
    ),
    path(
        'projeto05/pedidos/total-por-cidade-incluindo-cidades-sem-pedido',
        views.PedidosSomaPorCidadeIncluindoSemPedidos.as_view(),
        name='pedidos-media-por-cidade-incluindo-zero',
    ),
    path(
        'projeto05/pedidos/total-por-cidade-incluindo-cidades-sem-pedido-e-estado',  # noqa
        views.PedidosSomaPorCidadeIncluindoSemPedidosEEstado.as_view(),  # noqa
        name='pedidos-media-por-cidade-incluindo-cidades-sem-pedido-e-estado',
    ),
    path(
        'projeto05/vendas/carregar-dados',
        views.VendasLoadData.as_view(),
        name='vendas-carregar-dados',
    ),
    # path(
    #     'projeto04/times/carregar-dados',
    #     views.Projeto04TimesLoadFile.as_view(),
    #     name='times-carregar-dados',
    # ),
    # path(
    #     'projeto04/respostas/questao-1',
    #     views.Projeto04TecnicosAtletas.as_view(),
    #     name='respostas-tecnicos-atletas',
    # ),
]
