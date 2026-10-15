class PagamentoNaoEncontradoException(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Nenhum pagamento encontrado com o codigo {codigo}.")