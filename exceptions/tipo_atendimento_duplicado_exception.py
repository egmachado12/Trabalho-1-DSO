class TipoAtendimentoDuplicadoException(Exception):
    def __init__(self, nome: str):
        super().__init__(f"Ja existe um tipo de atendimento chamado {nome}.")
