from exceptions.atendimento_nao_encontrado_exception import AtendimentoNaoEncontradoException
from exceptions.pagamento_apos_data_exception import PagamentoAposDataException
from exceptions.pagamento_nao_encontrado_exception import PagamentoNaoEncontradoException
from exceptions.valor_excedente_exception import ValorExcedenteException
from model.atendimento import Atendimento
from model.pagamento import Pagamento
from view.tela_pagamento import TelaPagamento


class ControladorPagamentos:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pagamento = TelaPagamento()
        self.__pagamentos = []
        self.__proximo_codigo = 1

    @property
    def pagamentos(self) -> list:
        return self.__pagamentos

    #Busca

    def pega_pagamento_por_codigo(self, codigo: int) -> Pagamento:
        for pagamento in self.__pagamentos:
            if pagamento.codigo == codigo:
                return pagamento
        raise PagamentoNaoEncontradoException(codigo)

    #Valores pagos e restantes de um atendimento

    def valor_pago(self, atendimento: Atendimento) -> float:
        total = 0.0
        for pagamento in self.__pagamentos:
            if pagamento.atendimento is atendimento:
                total += pagamento.valor_pago
        return total

    def valor_restante(self, atendimento: Atendimento) -> float:
        return round(atendimento.valor_total() - self.valor_pago(atendimento), 2)

    #Regras de negocio do pagamento

    def __verifica_data(self, data, atendimento: Atendimento):
        if data > atendimento.data:
            raise PagamentoAposDataException(atendimento.data)

    def __verifica_valor(self, valor_pago: float, valor_restante: float):
        if valor_pago > valor_restante:
            raise ValorExcedenteException(valor_pago, valor_restante)

    #Inclusao, alteracao, exclusao e listagem

    def incluir(self):
        dados = self.__tela_pagamento.pega_dados_pagamento()
        try:
            controlador_atendimentos = self.__controlador_sistema.controlador_atendimentos
            atendimento = controlador_atendimentos.pega_atendimento_por_codigo(
                dados["codigo_atendimento"])
            self.__verifica_data(dados["data"], atendimento)
            self.__verifica_valor(dados["valor_pago"], self.valor_restante(atendimento))
            pagamento = Pagamento(self.__proximo_codigo, dados["data"], dados["valor_pago"],
                                  atendimento, atendimento.paciente,
                                  dados["tipo_forma"], dados["dados_forma"])
            self.__pagamentos.append(pagamento)
            self.__proximo_codigo += 1
            self.__tela_pagamento.mostra_mensagem(
                f"Pagamento {pagamento.codigo} registrado com sucesso! "
                f"Restante do atendimento: R${self.valor_restante(atendimento):.2f}.")
        except (AtendimentoNaoEncontradoException, PagamentoAposDataException,
                ValorExcedenteException) as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))

    def alterar(self):
        if not self.__tem_pagamentos():
            return
        self.listar()
        try:
            pagamento = self.pega_pagamento_por_codigo(self.__tela_pagamento.seleciona_pagamento())
            dados = self.__tela_pagamento.pega_dados_pagamento(alterando=True)
            atendimento = pagamento.atendimento
            self.__verifica_data(dados["data"], atendimento)
            restante_sem_este = round(self.valor_restante(atendimento) + pagamento.valor_pago, 2)
            self.__verifica_valor(dados["valor_pago"], restante_sem_este)
            pagamento.data = dados["data"]
            pagamento.valor_pago = dados["valor_pago"]
            pagamento.definir_forma_pagamento(dados["tipo_forma"], dados["dados_forma"])
            self.__tela_pagamento.mostra_mensagem("Pagamento alterado com sucesso!")
        except (PagamentoNaoEncontradoException, PagamentoAposDataException,
                ValorExcedenteException) as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))

    def excluir(self):
        if not self.__tem_pagamentos():
            return
        self.listar()
        try:
            pagamento = self.pega_pagamento_por_codigo(self.__tela_pagamento.seleciona_pagamento())
            self.__pagamentos.remove(pagamento)
            self.__tela_pagamento.mostra_mensagem("Pagamento excluido com sucesso!")
        except PagamentoNaoEncontradoException as erro:
            self.__tela_pagamento.mostra_mensagem(str(erro))

    def listar(self):
        if not self.__tem_pagamentos():
            return
        for pagamento in self.__pagamentos:
            atendimento = pagamento.atendimento
            self.__tela_pagamento.mostra_pagamento({
                "codigo": pagamento.codigo,
                "atendimento": atendimento.codigo,
                "paciente": pagamento.paciente.nome,
                "data": pagamento.data.strftime("%d/%m/%Y"),
                "valor pago": f"R${pagamento.valor_pago:.2f}",
                "forma de pagamento": pagamento.forma_pagamento.descricao(),
                "restante do atendimento": f"R${self.valor_restante(atendimento):.2f}",
            })

    def __tem_pagamentos(self) -> bool:
        if not self.__pagamentos:
            self.__tela_pagamento.mostra_mensagem("Nenhum pagamento registrado.")
            return False
        return True

    #Menu

    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar,
        }
        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            if opcao == 0:
                return
            opcoes[opcao]()
