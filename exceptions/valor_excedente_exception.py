class ValorExcedenteException(Exception):
    def __init__(self, valor_pago: float, valor_restante: float):
        super().__init__(f"O valor pago de R${valor_pago:.2f} excede o restante a pagar deste atendimento. "
                         f"Restante a pagar: R${valor_restante:.2f}.")