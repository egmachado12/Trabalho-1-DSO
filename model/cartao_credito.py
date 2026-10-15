from model.forma_pagamento import FormaPagamento


class CartaoCredito(FormaPagamento):
    def __init__(self, numero_cartao: str, bandeira: str):
        self.__numero_cartao = None
        self.numero_cartao = numero_cartao
        self.__bandeira = None
        self.bandeira = bandeira

    @property
    def numero_cartao(self) -> str:
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao

    @property
    def bandeira(self) -> str:
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str):
        if isinstance(bandeira, str):
            self.__bandeira = bandeira

    def descricao(self) -> str:
        return f"Cartao; Numero:{self.numero_cartao}, Bandeira:{self.bandeira}." 

