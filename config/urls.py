from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('home/', IndexView.as_view(), name='index'),
    path('cardapio-dia/', CardapioDiaView.as_view(), name='cardapio_dia'),
    path('refeicoes/', RefeicoesView.as_view(), name='refeicoes'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('sugestoes/', SugestoesView.as_view(), name='sugestoes'),
    path('avisos/', AvisosView.as_view(), name='avisos'),
]