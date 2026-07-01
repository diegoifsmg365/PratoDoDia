from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from datetime import date


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'visitante':
            request.session['perfil'] = 'visitante'
            return redirect('index')
        
        elif acao == 'login':
            nome = request.POST.get('nome')
            senha = request.POST.get('senha')
            
            try:
                usuario = Usuario.objects.get(nome=nome, senha=senha)
                
                if usuario.tipoUsuario.nivelAcesso in ['Nutricionista', 'Total']:
                    request.session['perfil'] = 'nutricionista'
                    return redirect('index')
                else:
                    request.session['perfil'] = 'visitante'
                    return redirect('index')
            except:
                return render(request, 'login.html', {'erro': 'Usuário ou senha incorretos.'})


class IndexView(View):
    def get(self, request, *args, **kwargs):
        cardapios_dia = CardapioDia.objects.all()
        avisos = Aviso.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'index.html', {
            'cardapios_dia': cardapios_dia,
            'avisos': avisos,
            'perfil': perfil
        })


class CardapioDiaView(View):
    def get(self, request, *args, **kwargs):
        cardapios = CardapioDia.objects.all()
        refeicoes = Refeicao.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'cardapio_dia.html', {
            'cardapios': cardapios,
            'refeicoes': refeicoes,
            'perfil': perfil
        })

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'adicionar':
            CardapioDia.objects.create(
                data=request.POST.get('data'),
                refeicaoAlmoco_id=request.POST.get('refeicaoAlmoco'),
                refeicaoJantar_id=request.POST.get('refeicaoJantar'),
            )
        
        elif acao == 'editar':
            cardapio = get_object_or_404(CardapioDia, id=request.POST.get('id'))
            cardapio.data = request.POST.get('data')
            cardapio.refeicaoAlmoco_id = request.POST.get('refeicaoAlmoco')
            cardapio.refeicaoJantar_id = request.POST.get('refeicaoJantar')
            cardapio.save()
        
        elif acao == 'excluir':
            cardapio = get_object_or_404(CardapioDia, id=request.POST.get('id'))
            cardapio.delete()
        
        return redirect('cardapio_dia')


class RefeicoesView(View):
    def get(self, request, *args, **kwargs):
        refeicoes = Refeicao.objects.all()
        dias = DiaSemana.objects.all()
        tipos = TipoRefeicao.objects.all()
        cardapios = CardapioSemanal.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'refeicoes.html', {
            'refeicoes': refeicoes,
            'dias': dias,
            'tipos': tipos,
            'cardapios': cardapios,
            'perfil': perfil
        })

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'adicionar':
            Refeicao.objects.create(
                diaSemana_id=request.POST.get('diaSemana'),
                tipoRefeicao_id=request.POST.get('tipoRefeicao'),
                pratoPrincipal=request.POST.get('pratoPrincipal'),
                opcaoVegetariana=request.POST.get('opcaoVegetariana'),
                acompanhamento=request.POST.get('acompanhamento'),
                salada=request.POST.get('salada'),
                sobremesa=request.POST.get('sobremesa'),
                suco=request.POST.get('suco'),
                cardapioSemanal_id=request.POST.get('cardapioSemanal'),
            )
        
        elif acao == 'editar':
            refeicao = get_object_or_404(Refeicao, id=request.POST.get('id'))
            refeicao.diaSemana_id = request.POST.get('diaSemana')
            refeicao.tipoRefeicao_id = request.POST.get('tipoRefeicao')
            refeicao.pratoPrincipal = request.POST.get('pratoPrincipal')
            refeicao.opcaoVegetariana = request.POST.get('opcaoVegetariana')
            refeicao.acompanhamento = request.POST.get('acompanhamento')
            refeicao.salada = request.POST.get('salada')
            refeicao.sobremesa = request.POST.get('sobremesa')
            refeicao.suco = request.POST.get('suco')
            refeicao.cardapioSemanal_id = request.POST.get('cardapioSemanal')
            refeicao.save()
        
        elif acao == 'excluir':
            refeicao = get_object_or_404(Refeicao, id=request.POST.get('id'))
            refeicao.delete()
        
        return redirect('refeicoes')


class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        usuarios = Usuario.objects.all()
        refeicoes = Refeicao.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'avaliacoes.html', {
            'avaliacoes': avaliacoes,
            'usuarios': usuarios,
            'refeicoes': refeicoes,
            'perfil': perfil
        })

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'adicionar':
            Avaliacao.objects.create(
                nota=request.POST.get('nota'),
                comentario=request.POST.get('comentario'),
                dataHora=request.POST.get('dataHora'),
                usuario_id=request.POST.get('usuario'),
                refeicao_id=request.POST.get('refeicao'),
            )
        
        elif acao == 'editar':
            avaliacao = get_object_or_404(Avaliacao, id=request.POST.get('id'))
            avaliacao.nota = request.POST.get('nota')
            avaliacao.comentario = request.POST.get('comentario')
            avaliacao.dataHora = request.POST.get('dataHora')
            avaliacao.usuario_id = request.POST.get('usuario')
            avaliacao.refeicao_id = request.POST.get('refeicao')
            avaliacao.save()
        
        elif acao == 'excluir':
            avaliacao = get_object_or_404(Avaliacao, id=request.POST.get('id'))
            avaliacao.delete()
        
        return redirect('avaliacoes')


class SugestoesView(View):
    def get(self, request, *args, **kwargs):
        sugestoes = Sugestao.objects.all()
        usuarios = Usuario.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'sugestoes.html', {
            'sugestoes': sugestoes,
            'usuarios': usuarios,
            'perfil': perfil
        })

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'adicionar':
            Sugestao.objects.create(
                titulo=request.POST.get('titulo'),
                descricao=request.POST.get('descricao'),
                dataHora=request.POST.get('dataHora'),
                status=request.POST.get('status'),
                usuario_id=request.POST.get('usuario'),
            )
        
        elif acao == 'editar':
            sugestao = get_object_or_404(Sugestao, id=request.POST.get('id'))
            sugestao.titulo = request.POST.get('titulo')
            sugestao.descricao = request.POST.get('descricao')
            sugestao.dataHora = request.POST.get('dataHora')
            sugestao.status = request.POST.get('status')
            sugestao.usuario_id = request.POST.get('usuario')
            sugestao.save()
        
        elif acao == 'excluir':
            sugestao = get_object_or_404(Sugestao, id=request.POST.get('id'))
            sugestao.delete()
        
        return redirect('sugestoes')


class AvisosView(View):
    def get(self, request, *args, **kwargs):
        avisos = Aviso.objects.all()
        usuarios = Usuario.objects.all()
        perfil = request.session.get('perfil', 'visitante')
        return render(request, 'avisos.html', {
            'avisos': avisos,
            'usuarios': usuarios,
            'perfil': perfil
        })

    def post(self, request, *args, **kwargs):
        acao = request.POST.get('acao')
        
        if acao == 'adicionar':
            Aviso.objects.create(
                titulo=request.POST.get('titulo'),
                mensagem=request.POST.get('mensagem'),
                dataPublicacao=request.POST.get('dataPublicacao'),
                dataExpiracao=request.POST.get('dataExpiracao'),
                usuario_id=request.POST.get('usuario'),
            )
        
        elif acao == 'editar':
            aviso = get_object_or_404(Aviso, id=request.POST.get('id'))
            aviso.titulo = request.POST.get('titulo')
            aviso.mensagem = request.POST.get('mensagem')
            aviso.dataPublicacao = request.POST.get('dataPublicacao')
            aviso.dataExpiracao = request.POST.get('dataExpiracao')
            aviso.usuario_id = request.POST.get('usuario')
            aviso.save()
        
        elif acao == 'excluir':
            aviso = get_object_or_404(Aviso, id=request.POST.get('id'))
            aviso.delete()
        
        return redirect('avisos')