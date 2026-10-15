from model.paciente import Paciente


class PacienteMenorDeIdadeException(Exception):
    def __init__(self, paciente: Paciente):
        super().__init__(f"O paciente {paciente.nome} tem {paciente.idade()} anos. "
                         f"Somente pacientes de 18 anos ou mais podem ser atendidos.")