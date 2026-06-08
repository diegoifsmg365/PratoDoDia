from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cardapio-dia/', CardapioDiaView.as_view(), name='cardapio_dia'),
    path('cardapio-semanal/', CardapioSemanalView.as_view(), name='cardapio_semanal'),
    path('refeicoes/', RefeicoesView.as_view(), name='refeicoes'),
    path('tipo-refeicao/', TipoRefeicaoView.as_view(), name='tipo_refeicao'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('dia-semana/', DiaSemanaView.as_view(), name='dia_semana'),
    path('sugestoes/', SugestoesView.as_view(), name='sugestoes'),
    path('tipo-usuario/', TipoUsuarioView.as_view(), name='tipo_usuario'),
    path('avisos/', AvisosView.as_view(), name='avisos'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('restricoes/', RestricoesAlimentaresView.as_view(), name='restricoes'),
    path('fotos/', FotosRefeicaoView.as_view(), name='fotos'),
    path('medias/', MediaAvaliacaoView.as_view(), name='medias'),
]