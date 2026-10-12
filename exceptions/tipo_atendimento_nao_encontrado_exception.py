class TipoAtendimentoNaoEncontradoException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Nenhum tipo de atendimento encontrado com o nome {nome}.")
