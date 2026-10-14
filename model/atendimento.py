from datetime import time, date

from model.clinica import Clinica
from model.profissional import Profissional
from model.tipo_atendimento import TipoAtendimento
from model.paciente import Paciente
#procedimento

class Atendimento:
    def __init__(self, codigo: int, data: date, hora_inicio: time, hora_fim: time, valor: float, clinica: Clinica,
                  profissional: Profissional, tipo_atendimento: TipoAtendimento, paciente: Paciente):
        self.__codigo = None
        self.codigo = codigo
        self.__data = None
        self.data = data
        self.__hora_inicio = None
        self.hora_inicio = hora_inicio
        self.__hora_fim = None
        self.hora_fim = hora_fim
        self.__valor = None
        self.valor = valor
        self.__clinica = None
        self.clinica = clinica
        self.__profissional = None
        self.profissional = profissional
        self.__tipo_atendimento = None
        self.tipo_atendimento = tipo_atendimento
        self.__paciente = None
        self.paciente = paciente
        self.__procedimentos = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data

    @property
    def hora_inicio(self) -> time:
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: time):
        if isinstance(hora_inicio, time):
            self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self) -> time:
        return self.__hora_fim

    @hora_fim.setter
    def hora_fim(self, hora_fim: time):
        if isinstance(hora_fim, time):
            self.__hora_fim = hora_fim

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, (int, float)):
            self.__valor = float(valor)

    @property
    def clinica(self) -> Clinica:
        return self.__clinica

    @clinica.setter
    def clinica(self, clinica: Clinica):
        if isinstance(clinica, Clinica):
            self.__clinica = clinica

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional

    @property
    def tipo_atendimento(self) -> TipoAtendimento:
        return self.__tipo_atendimento

    @tipo_atendimento.setter
    def tipo_atendimento(self, tipo_atendimento: TipoAtendimento):
        if isinstance(tipo_atendimento, TipoAtendimento):
            self.__tipo_atendimento = tipo_atendimento

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente