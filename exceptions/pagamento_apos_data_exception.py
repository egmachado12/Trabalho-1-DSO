from datetime import date


class PagamentoAposDataException(Exception):
    def __init__(self, data_atendimento: date):
        data_formatada = data_atendimento.strftime('%d/%m/%Y')
        super().__init__(f"O pagamento tem que ser realizado ate a data do atendimento {data_formatada}.")

        
        