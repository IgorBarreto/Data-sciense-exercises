from django.urls import path
from projeto4 import views


urlpatterns = [
    path(
        'projeto04/atletas/carregar-dados',
        views.AtletasLoadFile.as_view(),
        name='atletas-carregar-dados',
    ),
    path(
        'projeto04/treinadores/carregar-dados',
        views.TreinadoresLoadFile.as_view(),
        name='treinadores-carregar-dados',
    ),
    path(
        'projeto04/registros/carregar-dados',
        views.RegistrosLoadFile.as_view(),
        name='registros-carregar-dados',
    ),
    path(
        'projeto04/medalhas/carregar-dados',
        views.MedalhasLoadFile.as_view(),
        name='medalhas-carregar-dados',
    ),
    path(
        'projeto04/times/carregar-dados',
        views.TimesLoadFile.as_view(),
        name='times-carregar-dados',
    ),
    path(
        'projeto04/respostas/questao-1',
        views.TecnicosAtletas.as_view(),
        name='respostas-tecnicos-atletas',
    ),
]
