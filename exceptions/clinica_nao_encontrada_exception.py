class ClinicaNaoEncontradaException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Nenhuma clinica encontrada com o nome {nome}.")
