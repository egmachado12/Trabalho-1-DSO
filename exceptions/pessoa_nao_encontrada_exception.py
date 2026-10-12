class PessoaNaoEncontradaException(Exception):
    def __init__(self, cpf: str):
        super().__init__(f"Nenhuma pessoa encontrada com o CPF {cpf}.")
