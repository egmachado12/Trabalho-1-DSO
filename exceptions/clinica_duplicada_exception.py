class ClinicaDuplicadaException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Ja existe uma clinica cadastrada com o nome {nome}.")
