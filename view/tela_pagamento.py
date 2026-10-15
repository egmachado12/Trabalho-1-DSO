from datetime import datetime


class TelaPagamento:
    def tela_opcoes(self) -> int:
        print()
        print("----- PAGAMENTOS -----")
        print("1 - Incluir pagamento")
        print("2 - Alterar pagamento")
        print("3 - Excluir pagamento")
        print("4 - Listar pagamentos")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4])

    def pega_dados_pagamento(self, alterando: bool = False) -> dict:
        print("--- Dados do pagamento ---")
        dados = {}
        if not alterando:
            dados["codigo_atendimento"] = self.le_codigo("Codigo do atendimento: ")
        dados["data"] = self.le_data("Data do pagamento (dd/mm/aaaa): ")
        dados["valor_pago"] = self.le_float("Valor pago: ")
        dados.update(self.pega_forma_pagamento())
        return dados

    def pega_forma_pagamento(self) -> dict:
        print("--- Forma de pagamento ---")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartao de credito")
        opcao = self.le_inteiro("Escolha a forma: ", [1, 2, 3])
        if opcao == 1:
            return {"tipo_forma": "dinheiro", "dados_forma": {}}
        if opcao == 2:
            return {"tipo_forma": "pix",
                    "dados_forma": {"cpf_pagador": self.le_texto("CPF do pagador: ")}}
        return {"tipo_forma": "cartao",
                "dados_forma": {"numero_cartao": self.le_texto("Numero do cartao: "),
                                "bandeira": self.le_texto("Bandeira: ")}}

    def seleciona_pagamento(self) -> int:
        return self.le_codigo("Digite o codigo do pagamento: ")

    def mostra_pagamento(self, dados: dict):
        print("-----")
        for campo, valor in dados.items():
            print(f"{campo}: {valor}")

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)

    def le_inteiro(self, mensagem: str, validos: list) -> int:
        while True:
            try:
                valor = int(input(mensagem))
                if valor not in validos:
                    raise ValueError
                return valor
            except ValueError:
                print("Opcao invalida! Digite um dos numeros:", validos)

    def le_codigo(self, mensagem: str) -> int:
        while True:
            try:
                codigo = int(input(mensagem))
                if codigo <= 0:
                    raise ValueError
                return codigo
            except ValueError:
                print("Codigo invalido! Digite um numero inteiro maior que zero.")

    def le_texto(self, mensagem: str) -> str:
        while True:
            texto = input(mensagem).strip()
            if texto:
                return texto
            print("Este campo nao pode ficar vazio.")

    def le_data(self, mensagem: str):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data invalida! Use o formato dd/mm/aaaa.")

    def le_float(self, mensagem: str) -> float:
        while True:
            try:
                valor = float(input(mensagem).replace(",", "."))
                if valor <= 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Valor invalido! Digite um numero maior que zero.")
