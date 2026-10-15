class SemDadosRelatorioException(Exception):
    def __init__(self, motivo: str):
        super().__init__(f"Nao ha dados para gerar o relatorio: {motivo}")
