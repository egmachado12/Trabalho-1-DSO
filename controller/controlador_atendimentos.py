from exceptions.atendimento_nao_encontrado_exception import AtendimentoNaoEncontradoException
from exceptions.clinica_nao_encontrada_exception import ClinicaNaoEncontradaException
from exceptions.fora_do_horario_exception import ForaDoHorarioException
from exceptions.paciente_menor_de_idade_exception import PacienteMenorDeIdadeException
from exceptions.pessoa_nao_encontrada_exception import PessoaNaoEncontradaException
from exceptions.procedimento_nao_encontrado_exception import ProcedimentoNaoEncontradoException
from exceptions.tipo_atendimento_nao_encontrado_exception import (
    TipoAtendimentoNaoEncontradoException,
)
from model.atendimento import Atendimento
from model.procedimento import Procedimento
from view.tela_atendimento import TelaAtendimento


class ControladorAtendimentos:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_atendimento = TelaAtendimento()
        self.__atendimentos = []
        self.__proximo_codigo = 1

    @property
    def atendimentos(self) -> list:
        return self.__atendimentos

    #Buscas
    def pega_atendimento_por_codigo(self, codigo: int) -> Atendimento:
        for atendimento in self.__atendimentos:
            if atendimento.codigo == codigo:
                return atendimento
        raise AtendimentoNaoEncontradoException(codigo)

    def __pega_procedimento_por_descricao(self, atendimento: Atendimento,
                                          descricao: str) -> Procedimento:
        for procedimento in atendimento.procedimentos:
            if procedimento.descricao.lower() == descricao.lower():
                return procedimento
        raise ProcedimentoNaoEncontradoException(descricao)

    #Regras de negocio do atendimento
    def __busca_participantes(self, dados: dict) -> dict:
        controlador_pessoas = self.__controlador_sistema.controlador_pessoas
        controlador_clinicas = self.__controlador_sistema.controlador_clinicas
        controlador_tipos = self.__controlador_sistema.controlador_tipos_atendimento
        return {
            "paciente": controlador_pessoas.pega_paciente_por_cpf(dados["cpf_paciente"]),
            "profissional": controlador_pessoas.pega_profissional_por_cpf(
                dados["cpf_profissional"]),
            "clinica": controlador_clinicas.pega_clinica_por_nome(dados["nome_clinica"]),
            "tipo": controlador_tipos.pega_tipo_por_nome(dados["nome_tipo"]),
        }

    def __verifica_regras(self, participantes: dict, dados: dict):
        paciente = participantes["paciente"]
        if not paciente.maior_de_idade():
            raise PacienteMenorDeIdadeException(paciente)
        clinica = participantes["clinica"]
        if not clinica.esta_aberta(dados["hora_inicio"], dados["hora_fim"]):
            raise ForaDoHorarioException(clinica)

    #Inclusao, alteracao, exclusao e listagem
    def incluir(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()
        try:
            participantes = self.__busca_participantes(dados)
            self.__verifica_regras(participantes, dados)
            atendimento = Atendimento(self.__proximo_codigo, dados["data"],
                                      dados["hora_inicio"], dados["hora_fim"], dados["valor"],
                                      participantes["clinica"], participantes["profissional"],
                                      participantes["tipo"], participantes["paciente"])
            self.__atendimentos.append(atendimento)
            self.__proximo_codigo += 1
            self.__tela_atendimento.mostra_mensagem(
                f"Atendimento {atendimento.codigo} cadastrado com sucesso!")
        except (PessoaNaoEncontradaException, ClinicaNaoEncontradaException,
                TipoAtendimentoNaoEncontradoException, PacienteMenorDeIdadeException,
                ForaDoHorarioException) as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def alterar(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            dados = self.__tela_atendimento.pega_dados_atendimento()
            participantes = self.__busca_participantes(dados)
            self.__verifica_regras(participantes, dados)
            atendimento.data = dados["data"]
            atendimento.hora_inicio = dados["hora_inicio"]
            atendimento.hora_fim = dados["hora_fim"]
            atendimento.valor = dados["valor"]
            atendimento.clinica = participantes["clinica"]
            atendimento.profissional = participantes["profissional"]
            atendimento.tipo_atendimento = participantes["tipo"]
            atendimento.paciente = participantes["paciente"]
            self.__tela_atendimento.mostra_mensagem("Atendimento alterado com sucesso!")
        except (AtendimentoNaoEncontradoException, PessoaNaoEncontradaException,
                ClinicaNaoEncontradaException, TipoAtendimentoNaoEncontradoException,
                PacienteMenorDeIdadeException, ForaDoHorarioException) as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def excluir(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            controlador_pagamentos = self.__controlador_sistema.controlador_pagamentos
            if controlador_pagamentos.valor_pago(atendimento) > 0:
                self.__tela_atendimento.mostra_mensagem(
                    "Esse atendimento possui pagamentos. Exclua os pagamentos antes.")
                return
            self.__atendimentos.remove(atendimento)
            self.__tela_atendimento.mostra_mensagem("Atendimento excluido com sucesso!")
        except AtendimentoNaoEncontradoException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def listar(self):
        if not self.__tem_atendimentos():
            return
        controlador_pagamentos = self.__controlador_sistema.controlador_pagamentos
        for atendimento in self.__atendimentos:
            self.__tela_atendimento.mostra_atendimento({
                "codigo": atendimento.codigo,
                "data": atendimento.data.strftime("%d/%m/%Y"),
                "horario": f"{atendimento.hora_inicio.strftime('%H:%M')} "
                           f"as {atendimento.hora_fim.strftime('%H:%M')}",
                "clinica": atendimento.clinica.nome,
                "tipo": atendimento.tipo_atendimento.nome,
                "paciente": atendimento.paciente.nome,
                "profissional": atendimento.profissional.nome,
                "valor": f"R${atendimento.valor:.2f}",
                "procedimentos": len(atendimento.procedimentos),
                "valor total": f"R${atendimento.valor_total():.2f}",
                "valor pago": f"R${controlador_pagamentos.valor_pago(atendimento):.2f}",
                "restante": f"R${controlador_pagamentos.valor_restante(atendimento):.2f}",
            })

    def __tem_atendimentos(self) -> bool:
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem("Nenhum atendimento cadastrado.")
            return False
        return True

    #Procedimentos do atendimento (composicao)
    def incluir_procedimento(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            dados = self.__tela_atendimento.pega_dados_procedimento()
            controlador_pessoas = self.__controlador_sistema.controlador_pessoas
            profissional = controlador_pessoas.pega_profissional_por_cpf(
                dados["cpf_profissional"])
            atendimento.adicionar_procedimento(dados["descricao"], dados["custo"], profissional)
            self.__tela_atendimento.mostra_mensagem("Procedimento incluido com sucesso!")
        except (AtendimentoNaoEncontradoException, PessoaNaoEncontradaException) as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def alterar_procedimento(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            if not self.__mostra_procedimentos(atendimento):
                return
            procedimento = self.__pega_procedimento_por_descricao(
                atendimento, self.__tela_atendimento.seleciona_procedimento())
            dados = self.__tela_atendimento.pega_dados_procedimento()
            controlador_pessoas = self.__controlador_sistema.controlador_pessoas
            profissional = controlador_pessoas.pega_profissional_por_cpf(
                dados["cpf_profissional"])
            procedimento.descricao = dados["descricao"]
            procedimento.custo = dados["custo"]
            procedimento.profissional = profissional
            self.__tela_atendimento.mostra_mensagem("Procedimento alterado com sucesso!")
        except (AtendimentoNaoEncontradoException, ProcedimentoNaoEncontradoException,
                PessoaNaoEncontradaException) as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def excluir_procedimento(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            if not self.__mostra_procedimentos(atendimento):
                return
            procedimento = self.__pega_procedimento_por_descricao(
                atendimento, self.__tela_atendimento.seleciona_procedimento())
            atendimento.remover_procedimento(procedimento)
            self.__tela_atendimento.mostra_mensagem("Procedimento excluido com sucesso!")
        except (AtendimentoNaoEncontradoException, ProcedimentoNaoEncontradoException) as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def listar_procedimentos(self):
        if not self.__tem_atendimentos():
            return
        self.listar()
        try:
            atendimento = self.pega_atendimento_por_codigo(
                self.__tela_atendimento.seleciona_atendimento())
            self.__mostra_procedimentos(atendimento)
        except AtendimentoNaoEncontradoException as erro:
            self.__tela_atendimento.mostra_mensagem(str(erro))

    def __mostra_procedimentos(self, atendimento: Atendimento) -> bool:
        if not atendimento.procedimentos:
            self.__tela_atendimento.mostra_mensagem(
                f"O atendimento {atendimento.codigo} nao tem procedimentos.")
            return False
        for procedimento in atendimento.procedimentos:
            self.__tela_atendimento.mostra_procedimento({
                "descricao": procedimento.descricao,
                "custo": f"R${procedimento.custo:.2f}",
                "profissional": procedimento.profissional.nome,
            })
        return True

    #Menu
    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar,
            5: self.incluir_procedimento,
            6: self.alterar_procedimento,
            7: self.excluir_procedimento,
            8: self.listar_procedimentos,
        }
        while True:
            opcao = self.__tela_atendimento.tela_opcoes()
            if opcao == 0:
                return
            opcoes[opcao]()
