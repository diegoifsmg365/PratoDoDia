from django.db import models


# RF08 - Gerenciar o tipo de usuário
class TipoUsuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do tipo de usuário")
    nivelAcesso = models.CharField(max_length=20, verbose_name="Nível de acesso")

    def __str__(self):
        return f"{self.nome}, {self.nivelAcesso}"

    class Meta:
        verbose_name = "Tipo de Usuário"
        verbose_name_plural = "Tipos de Usuário"


# RF06 - Gerenciar os dias da semana
class DiaSemana(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome do dia")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Dia da Semana"
        verbose_name_plural = "Dias da Semana"


# RF04 - Gerenciar tipos de refeição
class TipoRefeicao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do tipo de refeição")
    horarioInicio = models.TimeField(verbose_name="Horário de início")
    horarioFim = models.TimeField(verbose_name="Horário de fim")

    def __str__(self):
        return f"{self.nome}, {self.horarioInicio} - {self.horarioFim}"

    class Meta:
        verbose_name = "Tipo de Refeição"
        verbose_name_plural = "Tipos de Refeição"


# RF01 - Gerenciar usuários do sistema
class Usuario(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome do usuário")
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula do usuário")
    email = models.CharField(max_length=100, verbose_name="Email do usuário")
    senha = models.CharField(max_length=128, verbose_name="Senha do usuário")
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, verbose_name="Tipo de usuário")

    def __str__(self):
        return f"{self.nome}, {self.tipoUsuario.nome}"

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


# RF02 - Gerenciar o cardápio semanal
class CardapioSemanal(models.Model):
    dataInicio = models.DateField(verbose_name="Data de início")
    dataFim = models.DateField(verbose_name="Data de fim")
    status = models.CharField(max_length=20, verbose_name="Status do cardápio")

    def __str__(self):
        return f"Cardápio {self.dataInicio} a {self.dataFim}, {self.status}"

    class Meta:
        verbose_name = "Cardápio Semanal"
        verbose_name_plural = "Cardápios Semanais"


# RF03 - Gerenciar refeições do cardápio
class Refeicao(models.Model):
    pratoPrincipal = models.CharField(max_length=200, verbose_name="Prato principal")
    opcaoVegetariana = models.CharField(max_length=200, verbose_name="Opção vegetariana")
    acompanhamento = models.CharField(max_length=200, verbose_name="Acompanhamento")
    salada = models.CharField(max_length=200, verbose_name="Salada")
    sobremesa = models.CharField(max_length=200, verbose_name="Sobremesa")
    suco = models.CharField(max_length=100, verbose_name="Suco")
    diaSemana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE, verbose_name="Dia da semana")
    tipoRefeicao = models.ForeignKey(TipoRefeicao, on_delete=models.CASCADE, verbose_name="Tipo de refeição")
    cardapioSemanal = models.ForeignKey(CardapioSemanal, on_delete=models.CASCADE, verbose_name="Cardápio semanal")

    def __str__(self):
        return f"{self.diaSemana.nome}, {self.tipoRefeicao.nome}, {self.pratoPrincipal}"

    class Meta:
        verbose_name = "Refeição"
        verbose_name_plural = "Refeições"


# RF05 - Gerenciar avaliações dos alunos sobre as refeições
class Avaliacao(models.Model):
    nota = models.IntegerField(verbose_name="Nota da avaliação")
    comentario = models.TextField(verbose_name="Comentário da avaliação")
    dataHora = models.DateTimeField(verbose_name="Data e hora da avaliação")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário que avaliou")
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição avaliada")

    def __str__(self):
        return f"Nota {self.nota}, {self.usuario.nome}, {self.refeicao}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


# RF07 - Gerenciar o feedback e sugestões gerais dos alunos
class Sugestao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da sugestão")
    descricao = models.TextField(verbose_name="Descrição da sugestão")
    dataHora = models.DateTimeField(verbose_name="Data e hora da sugestão")
    status = models.CharField(max_length=20, verbose_name="Status da sugestão")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário que sugeriu")

    def __str__(self):
        return f"{self.titulo}, {self.usuario.nome}, {self.status}"

    class Meta:
        verbose_name = "Sugestão"
        verbose_name_plural = "Sugestões"


# RF09 - Gerenciar notificações e avisos do refeitório
class Aviso(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título do aviso")
    mensagem = models.TextField(verbose_name="Mensagem do aviso")
    dataPublicacao = models.DateTimeField(verbose_name="Data de publicação")
    dataExpiracao = models.DateTimeField(verbose_name="Data de expiração")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuário que publicou")

    def __str__(self):
        return f"{self.titulo}, {self.dataExpiracao}"

    class Meta:
        verbose_name = "Aviso"
        verbose_name_plural = "Avisos"


# RF010 - Gerenciar o cardápio do dia (visão simplificada)
class CardapioDia(models.Model):
    data = models.DateField(verbose_name="Data do cardápio")
    refeicaoAlmoco = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição do almoço", related_name="cardapio_almoco")
    refeicaoJantar = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição do jantar", related_name="cardapio_jantar")

    def __str__(self):
        return f"Cardápio do dia {self.data}"

    class Meta:
        verbose_name = "Cardápio do Dia"
        verbose_name_plural = "Cardápios do Dia"


# RF011 - Gerenciar ingredientes ou restrições alimentares
class RestricaoAlimentar(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da restrição")
    descricao = models.TextField(verbose_name="Descrição da restrição")
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição relacionada")

    def __str__(self):
        return f"{self.nome}, {self.refeicao}"

    class Meta:
        verbose_name = "Restrição Alimentar"
        verbose_name_plural = "Restrições Alimentares"


# RF012 - Gerenciar fotos das refeições
class FotoRefeicao(models.Model):
    urlFoto = models.CharField(max_length=300, verbose_name="URL da foto")
    legenda = models.CharField(max_length=200, verbose_name="Legenda da foto")
    dataUpload = models.DateTimeField(verbose_name="Data de upload")
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição relacionada")

    def __str__(self):
        return f"Foto: {self.refeicao}"

    class Meta:
        verbose_name = "Foto da Refeição"
        verbose_name_plural = "Fotos das Refeições"


# RF013 - Gerenciar a média de avaliações por refeição
class MediaAvaliacao(models.Model):
    notaMedia = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Nota média")
    quantidadeAvaliacoes = models.IntegerField(verbose_name="Quantidade de avaliações")
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE, verbose_name="Refeição relacionada")

    def __str__(self):
        return f"Média {self.notaMedia}, {self.quantidadeAvaliacoes} avaliações, {self.refeicao}"

    class Meta:
        verbose_name = "Média de Avaliação"
        verbose_name_plural = "Médias de Avaliações"