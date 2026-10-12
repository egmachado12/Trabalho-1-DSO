from datetime import date

from model.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, data_nascimento: date):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = None
        self.data_nascimento = data_nascimento

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento

    def idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year
        ainda_nao_fez_aniversario = (hoje.month, hoje.day) < (
            self.__data_nascimento.month,
            self.__data_nascimento.day,
        )
        if ainda_nao_fez_aniversario:
            idade -= 1
        return idade

    def maior_de_idade(self) -> bool:
        return self.idade() >= 18
