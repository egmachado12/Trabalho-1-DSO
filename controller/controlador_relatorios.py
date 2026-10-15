from exceptions.sem_dados_relatorio_exception import SemDadosRelatorioException
from view.tela_relatorio import TelaRelatorio


class ControladorRelatorios:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_relatorio = TelaRelatorio()

    # ---------- Dados usados pelos relatorios ----------

    def __pega_atendimentos(self) -> list:
        atendimentos = self.__controlador_sistema.controlador_atendimentos.atendimentos
        if not atendimentos:
            raise SemDadosRelatorioException("nenhum atendimento cadastrado.")
        return atendimentos

    def __pega_procedimentos(self) -> list:
        procedimentos = []
        for atendimento in self.__pega_atendimentos():
            procedimentos.extend(atendimento.procedimentos)
        if not procedimentos:
            raise SemDadosRelatorioException("nenhum procedimento registrado.")
        return procedimentos

    def __descreve_atendimento(self, atendimento) -> str:
        return (f"Atendimento {atendimento.codigo} - {atendimento.data.strftime('%d/%m/%Y')} - "
                f"{atendimento.paciente.nome} na clinica {atendimento.clinica.nome} - "
                f"total R$ {atendimento.valor_total():.2f}")

    def __descreve_procedimento(self, procedimento) -> str:
        return (f"{procedimento.descricao} - R$ {procedimento.custo:.2f} - "
                f"profissional {procedimento.profissional.nome}")

    # ---------- Relatorios ----------

    def clinicas_com_mais_atendimentos(self):
        contagem = {}
        for atendimento in self.__pega_atendimentos():
            clinica = atendimento.clinica
            contagem[clinica] = contagem.get(clinica, 0) + 1
        ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        linhas = [f"{posicao}. {clinica.nome} ({clinica.cidade}): {quantidade} atendimento(s)"
                  for posicao, (clinica, quantidade) in enumerate(ranking, start=1)]
        self.__tela_relatorio.mostra_relatorio("CLINICAS COM MAIS ATENDIMENTOS", linhas)

    def atendimentos_mais_caros_e_baratos(self):
        atendimentos = self.__pega_atendimentos()
        maior = max(a.valor_total() for a in atendimentos)
        menor = min(a.valor_total() for a in atendimentos)
        linhas = ["Mais caro(s):"]
        linhas += ["  " + self.__descreve_atendimento(a)
                   for a in atendimentos if a.valor_total() == maior]
        linhas.append("Mais barato(s):")
        linhas += ["  " + self.__descreve_atendimento(a)
                   for a in atendimentos if a.valor_total() == menor]
        self.__tela_relatorio.mostra_relatorio("ATENDIMENTOS MAIS CAROS E MAIS BARATOS", linhas)

    def procedimentos_mais_realizados(self):
        contagem = {}
        for procedimento in self.__pega_procedimentos():
            nome = procedimento.descricao.strip().capitalize()
            contagem[nome] = contagem.get(nome, 0) + 1
        ranking = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
        linhas = [f"{posicao}. {nome}: realizado {quantidade} vez(es)"
                  for posicao, (nome, quantidade) in enumerate(ranking, start=1)]
        self.__tela_relatorio.mostra_relatorio("PROCEDIMENTOS MAIS REALIZADOS", linhas)

    def procedimentos_mais_caros_e_baratos(self):
        procedimentos = self.__pega_procedimentos()
        maior = max(p.custo for p in procedimentos)
        menor = min(p.custo for p in procedimentos)
        linhas = ["Mais caro(s):"]
        linhas += ["  " + self.__descreve_procedimento(p)
                   for p in procedimentos if p.custo == maior]
        linhas.append("Mais barato(s):")
        linhas += ["  " + self.__descreve_procedimento(p)
                   for p in procedimentos if p.custo == menor]
        self.__tela_relatorio.mostra_relatorio("PROCEDIMENTOS MAIS CAROS E MAIS BARATOS", linhas)

    # ---------- Menu ----------

    def abre_tela(self):
        opcoes = {
            1: self.clinicas_com_mais_atendimentos,
            2: self.atendimentos_mais_caros_e_baratos,
            3: self.procedimentos_mais_realizados,
            4: self.procedimentos_mais_caros_e_baratos,
        }
        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            if opcao == 0:
                return
            try:
                opcoes[opcao]()
            except SemDadosRelatorioException as erro:
                self.__tela_relatorio.mostra_mensagem(str(erro))
