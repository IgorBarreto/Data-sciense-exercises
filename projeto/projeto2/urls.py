from django.urls import path
from projeto2 import views

urlpatterns = [
    path(
        'projeto02/cancer-mama/carregar-dados',
        views.LoadFiles.as_view(),
        name='cancer-mama-carregar-dados',
    ),
    path(
        'projeto02/cancer-mama/binarizacao',
        views.Binarizacao.as_view(),
        name='cancer-mama-binarizacao',
    ),
    path(
        'projeto02/cancer-mama/gerando-dataset',
        views.BinarizacaoGerandoDataset.as_view(),
        name='cancer-mama-outfile',
    ),
]
