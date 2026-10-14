class ProcedimentoNaoEncontradoException(Exception):
    def __init__(self, descricao: str):
        super().__init__(f"Nenhum procedimento encontrado com a descricao {descricao}.")