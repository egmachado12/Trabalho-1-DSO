from datetime import datetime


class TelaClinica:
    def tela_opcoes(self) -> int:
        print()
        print("----- CLINICAS -----")
        print("1 - Incluir clinica")
        print("2 - Alterar clinica")
        print("3 - Excluir clinica")
        print("4 - Listar clinicas")
        print("5 - Adicionar profissional a uma clinica")
        print("6 - Remover profissional de uma clinica")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4, 5, 6])

    def pega_dados_clinica(self, alterando: bool = False) -> dict:
        print("--- Dados da clinica ---")
        dados = {}
        if not alterando:
            dados["nome"] = self.le_texto("Nome: ")
        dados["cidade"] = self.le_texto("Cidade: ")
        dados["descricao"] = self.le_texto("Descricao: ")
        while True:
            dados["hora_abertura"] = self.le_hora("Horario de abertura (hh:mm): ")
            dados["hora_fechamento"] = self.le_hora("Horario de fechamento (hh:mm): ")
            if dados["hora_abertura"] < dados["hora_fechamento"]:
                return dados
            print("O horario de abertura precisa ser antes do fechamento.")

    def seleciona_clinica(self) -> str:
        return self.le_texto("Digite o nome da clinica: ")

    def seleciona_cpf_profissional(self) -> str:
        return self.le_texto("Digite o CPF do profissional: ")

    def mostra_clinica(self, dados: dict):
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

    def le_hora(self, mensagem: str):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%H:%M").time()
            except ValueError:
                print("Horario invalido! Use o formato hh:mm, por exemplo 08:30.")
