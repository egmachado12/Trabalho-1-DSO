from datetime import date

from model.atendimento import Atendimento
from model.paciente import Paciente
from model.forma_pagamento import FormaPagamento
from model.dinheiro import Dinheiro
from model.pix import Pix
from model.cartao_credito import CartaoCredito



class Pagamento:
    def __init__(self, codigo: int, data: date, valor_pago: float,
                  atendimento: Atendimento, paciente: Paciente, tipo_forma: str, dados_forma: dict):
        self.__codigo = None
        self.codigo = codigo
        self.__data = None
        self.data = data
        self.__valor_pago = None
        self.valor_pago = valor_pago
        self.__atendimento = None
        self.atendimento = atendimento
        self.__paciente = None
        self.paciente = paciente
        self.__forma_pagamento = None
        self.definir_forma_pagamento(tipo_forma, dados_forma)

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def valor_pago(self) -> float:
        return self.__valor_pago

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        if isinstance(valor_pago, (int, float)):
            self.__valor_pago = float(valor_pago)

    @property
    def atendimento(self) -> Atendimento:
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        if isinstance(atendimento, Atendimento):
            self.__atendimento = atendimento

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente

    @property
    def forma_pagamento(self) -> FormaPagamento:
        return self.__forma_pagamento        

    def definir_forma_pagamento(self, tipo_forma, dados_forma):
        if tipo_forma == "dinheiro":
            self.__forma_pagamento = Dinheiro()
        elif tipo_forma == "pix":
            self.__forma_pagamento = Pix(dados_forma["cpf_pagador"])
        elif tipo_forma == "cartao":
            self.__forma_pagamento = CartaoCredito(dados_forma["numero_cartao"], dados_forma["bandeira"])