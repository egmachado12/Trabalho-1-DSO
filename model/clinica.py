from datetime import time

from model.profissional import Profissional


class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str,
                 hora_abertura: time, hora_fechamento: time):
        self.__nome = None
        self.__cidade = None
        self.__descricao = None
        self.__hora_abertura = None
        self.__hora_fechamento = None
        self.__profissionais = []
        self.nome = nome
        self.cidade = cidade
        self.descricao = descricao
        self.hora_abertura = hora_abertura
        self.hora_fechamento = hora_fechamento

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cidade(self) -> str:
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        if isinstance(cidade, str):
            self.__cidade = cidade

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def hora_abertura(self) -> time:
        return self.__hora_abertura

    @hora_abertura.setter
    def hora_abertura(self, hora_abertura: time):
        if isinstance(hora_abertura, time):
            self.__hora_abertura = hora_abertura

    @property
    def hora_fechamento(self) -> time:
        return self.__hora_fechamento

    @hora_fechamento.setter
    def hora_fechamento(self, hora_fechamento: time):
        if isinstance(hora_fechamento, time):
            self.__hora_fechamento = hora_fechamento

    @property
    def profissionais(self) -> list:
        return self.__profissionais

    def esta_aberta(self, inicio: time, fim: time) -> bool:
        return (self.__hora_abertura <= inicio
                and fim <= self.__hora_fechamento
                and inicio < fim)

    def adicionar_profissional(self, profissional: Profissional):
        if isinstance(profissional, Profissional) and profissional not in self.__profissionais:
            self.__profissionais.append(profissional)

    def remover_profissional(self, profissional: Profissional):
        if profissional in self.__profissionais:
            self.__profissionais.remove(profissional)
