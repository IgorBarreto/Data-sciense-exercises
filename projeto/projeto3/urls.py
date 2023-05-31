from django.urls import path
from projeto3 import views

urlpatterns = [
    # =================== URLS PARA CARGA DE DADOS ===================
    path(
        'projeto03/clientes/carregar-dados',
        views.Clientes.as_view(),
        name='projeto03-clientes-carregar-dados',
    ),
    path(
        'projeto03/pedidos/carregar-dados',
        views.Pedidos.as_view(),
        name='projeto03-pedidos-carregar-dados',
    ),
    path(
        'projeto03/vendedores/carregar-dados',
        views.Vendedores.as_view(),
        name='projeto03-vendedores-carregar-dados',
    ),
    #
    path(
        'projeto03/pedidos/clientes',
        views.PedidoCliente.as_view(),
        name='projeto03-pedidos-vendedores',
    ),
    path(
        'projeto03/pedidos/clientes/all/left-join',
        views.PedidoAllClienteLeftJoin.as_view(),
        name='projeto03-pedidos-clientes-all-left-join',
    ),
    path(
        'projeto03/pedidos/clientes/all/right-join',
        views.PedidoAllClienteRightJoin.as_view(),
        name='projeto03-pedidos-clientes-all-right-join',
    ),
    path(
        'projeto03/pedidos/clientes/vendedores',
        views.PedidoClienteVendedor.as_view(),
        name='projeto03-pedidos-vendedores-nomes',
    ),
    path(
        'projeto03/pedidos/datas/clientes/vendedores/order-by-cliente',
        views.PedidoDataClienteVendedorOrderByCliente.as_view(),
        name='projeto03-pedidos-datas-vendedores-order-by-cliente',
    ),
    path(
        'projeto03/clientes/mesma-cidade',
        views.ClienteMesmaCidade.as_view(),
        name='projeto03-clientes-mesma-cidade',
    ),
]
