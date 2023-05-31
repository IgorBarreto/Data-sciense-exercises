from django.urls import path
from projeto1 import views


urlpatterns = [
    path(
        'projeto01/navios/carregar-dados',
        views.NavioCreateView.as_view(),
        name='navios-carregar-dados',
    ),
    path(
        'projeto01/navios/questao01',
        views.NavioListviewQuestao1.as_view(),
        name='navios-questao01',
    ),
    path(
        'projeto01/navios/questao02',
        views.NavioListviewQuestao2.as_view(),
        name='navios-questao01',
    ),
    path(
        'projeto01/navios/questao03',
        views.NavioListviewQuestao3.as_view(),
        name='navios-questao03',
    ),
    path(
        'projeto01/navios/questao04',
        views.NavioListviewQuestao4.as_view(),
        name='navios-questao04',
    ),
    path(
        'projeto01/navios/questao05',
        views.NavioListviewQuestao5.as_view(),
        name='navios-questao05',
    ),
]
