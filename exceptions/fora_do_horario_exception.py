from model.clinica import Clinica


class ForaDoHorarioException(Exception):
    def __init__(self, clinica: Clinica):
        abertura = clinica.hora_abertura.strftime('%H:%M')
        fechamento = clinica.hora_fechamento.strftime('%H:%M')
        super().__init__(f"O atendimento precisa ocorrer dentro do horario de funcionamento "
                         f"da clinica {clinica.nome} ({abertura} as {fechamento}).")
