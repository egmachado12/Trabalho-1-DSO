from controller.controlador_atendimentos import ControladorAtendimentos
from controller.controlador_clinicas import ControladorClinicas
from controller.controlador_pagamentos import ControladorPagamentos
from controller.controlador_pessoas import ControladorPessoas
from controller.controlador_relatorios import ControladorRelatorios
from controller.controlador_tipos_atendimento import ControladorTiposAtendimento
from view.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pessoas = ControladorPessoas(self)
        self.__controlador_clinicas = ControladorClinicas(self)
        self.__controlador_tipos_atendimento = ControladorTiposAtendimento(self)
        self.__controlador_atendimentos = ControladorAtendimentos(self)
        self.__controlador_pagamentos = ControladorPagamentos(self)
        self.__controlador_relatorios = ControladorRelatorios(self)

    @property
    def controlador_pessoas(self) -> ControladorPessoas:
        return self.__controlador_pessoas

    @property
    def controlador_clinicas(self) -> ControladorClinicas:
        return self.__controlador_clinicas

    @property
    def controlador_tipos_atendimento(self) -> ControladorTiposAtendimento:
        return self.__controlador_tipos_atendimento

    @property
    def controlador_atendimentos(self) -> ControladorAtendimentos:
        return self.__controlador_atendimentos

    @property
    def controlador_pagamentos(self) -> ControladorPagamentos:
        return self.__controlador_pagamentos

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastra_pessoas,
            2: self.cadastra_clinicas,
            3: self.cadastra_tipos_atendimento,
            4: self.registra_atendimentos,
            5: self.registra_pagamentos,
            6: self.emite_relatorios,
            0: self.encerra_sistema,
        }
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()

    def cadastra_pessoas(self):
        self.__controlador_pessoas.abre_tela()

    def cadastra_clinicas(self):
        self.__controlador_clinicas.abre_tela()

    def cadastra_tipos_atendimento(self):
        self.__controlador_tipos_atendimento.abre_tela()

    def registra_atendimentos(self):
        self.__controlador_atendimentos.abre_tela()

    def registra_pagamentos(self):
        self.__controlador_pagamentos.abre_tela()

    def emite_relatorios(self):
        self.__controlador_relatorios.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_mensagem("Saindo do sistema...")
        exit(0)