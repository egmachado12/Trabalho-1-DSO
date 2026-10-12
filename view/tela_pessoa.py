from datetime import datetime


class TelaPessoa:
    def tela_opcoes(self) -> int:
        print()
        print("----- PESSOAS -----")
        print("1 - Incluir paciente")
        print("2 - Incluir profissional")
        print("3 - Alterar pessoa")
        print("4 - Excluir pessoa")
        print("5 - Listar pessoas")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4, 5])

    def pega_dados_paciente(self, alterando: bool = False) -> dict:
        print("--- Dados do paciente ---")
        dados = {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
        }
        if not alterando:
            dados["cpf"] = self.le_texto("CPF: ")
        dados["data_nascimento"] = self.le_data("Data de nascimento (dd/mm/aaaa): ")
        return dados

    def pega_dados_profissional(self, alterando: bool = False) -> dict:
        print("--- Dados do profissional ---")
        dados = {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
        }
        if not alterando:
            dados["cpf"] = self.le_texto("CPF: ")
        dados["especialidade"] = self.le_texto("Especialidade: ")
        dados["registro_profissional"] = self.le_texto("Registro profissional: ")
        return dados

    def seleciona_cpf(self) -> str:
        return self.le_texto("Digite o CPF da pessoa: ")

    def mostra_pessoa(self, dados: dict):
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
