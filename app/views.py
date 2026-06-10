from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class CardapioDiaView(View):
    def get(self, request, *args, **kwargs):
        cardapios = CardapioDia.objects.all()
        return render(request, 'cardapio_dia.html', {'cardapios': cardapios})


class CardapioSemanalView(View):
    def get(self, request, *args, **kwargs):
        cardapios = CardapioSemanal.objects.all()
        return render(request, 'cardapio_semanal.html', {'cardapios': cardapios})


class RefeicoesView(View):
    def get(self, request, *args, **kwargs):
        refeicoes = Refeicao.objects.all()
        return render(request, 'refeicoes.html', {'refeicoes': refeicoes})


class TipoRefeicaoView(View):
    def get(self, request, *args, **kwargs):
        tipos = TipoRefeicao.objects.all()
        return render(request, 'tipo_refeicao.html', {'tipos': tipos})


class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})


class DiaSemanaView(View):
    def get(self, request, *args, **kwargs):
        dias = DiaSemana.objects.all()
        return render(request, 'dia_semana.html', {'dias': dias})


class SugestoesView(View):
    def get(self, request, *args, **kwargs):
        sugestoes = Sugestao.objects.all()
        return render(request, 'sugestoes.html', {'sugestoes': sugestoes})


class TipoUsuarioView(View):
    def get(self, request, *args, **kwargs):
        tipos = TipoUsuario.objects.all()
        return render(request, 'tipo_usuario.html', {'tipos': tipos})


class AvisosView(View):
    def get(self, request, *args, **kwargs):
        avisos = Aviso.objects.all()
        return render(request, 'avisos.html', {'avisos': avisos})


class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})


class RestricoesAlimentaresView(View):
    def get(self, request, *args, **kwargs):
        restricoes = RestricaoAlimentar.objects.all()
        return render(request, 'restricoes.html', {'restricoes': restricoes})


class FotosRefeicaoView(View):
    def get(self, request, *args, **kwargs):
        fotos = FotoRefeicao.objects.all()
        return render(request, 'fotos.html', {'fotos': fotos})


class MediaAvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        medias = MediaAvaliacao.objects.all()
        return render(request, 'medias.html', {'medias': medias})