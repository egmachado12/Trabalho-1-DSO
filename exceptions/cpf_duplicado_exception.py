class CpfDuplicadoException(Exception):
    def __init__(self, cpf: str):
        super().__init__(f"Ja existe uma pessoa cadastrada com o CPF {cpf}.")
