from model.forma_pagamento import FormaPagamento


class Dinheiro(FormaPagamento):
    def descricao(self) -> str:
        return "Dinheiro"
        