class AtendimentoNaoEncontradoException(Exception):
    def __init__(self, codigo: int):
        super().__init__(f"Nenhum atendimento encontrado com o codigo {codigo}.")