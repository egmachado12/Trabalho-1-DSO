from datetime import datetime


class TelaAtendimento:
    def tela_opcoes(self) -> int:
        print()
        print("----- ATENDIMENTOS -----")
        print("1 - Incluir atendimento")
        print("2 - Alterar atendimento")
        print("3 - Excluir atendimento")
        print("4 - Listar atendimentos")
        print("5 - Incluir procedimento em um atendimento")
        print("6 - Alterar procedimento de um atendimento")
        print("7 - Excluir procedimento de um atendimento")
        print("8 - Listar procedimentos de um atendimento")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def pega_dados_atendimento(self) -> dict:
        print("--- Dados do atendimento ---")
        dados = {
            "cpf_paciente": self.le_texto("CPF do paciente: "),
            "cpf_profissional": self.le_texto("CPF do profissional: "),
            "nome_clinica": self.le_texto("Nome da clinica: "),
            "nome_tipo": self.le_texto("Tipo de atendimento (ex.: Consulta, Exame, Retorno): "),
            "data": self.le_data("Data (dd/mm/aaaa): "),
        }
        while True:
            dados["hora_inicio"] = self.le_hora("Horario de inicio (hh:mm): ")
            dados["hora_fim"] = self.le_hora("Horario de fim (hh:mm): ")
            if dados["hora_inicio"] < dados["hora_fim"]:
                break
            print("O horario de inicio precisa ser antes do horario de fim.")
        dados["valor"] = self.le_float("Valor do atendimento: ")
        return dados

    def pega_dados_procedimento(self) -> dict:
        print("--- Dados do procedimento ---")
        return {
            "descricao": self.le_texto("Descricao: "),
            "custo": self.le_float("Custo: "),
            "cpf_profissional": self.le_texto("CPF do profissional responsavel: "),
        }

    def seleciona_atendimento(self) -> int:
        return self.le_codigo("Digite o codigo do atendimento: ")

    def seleciona_procedimento(self) -> str:
        return self.le_texto("Digite a descricao do procedimento: ")

    def mostra_atendimento(self, dados: dict):
        print("-----")
        for campo, valor in dados.items():
            print(f"{campo}: {valor}")

    def mostra_procedimento(self, dados: dict):
        print("  -")
        for campo, valor in dados.items():
            print(f"  {campo}: {valor}")

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

    def le_hora(self, mensagem: str):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%H:%M").time()
            except ValueError:
                print("Horario invalido! Use o formato hh:mm, por exemplo 08:30.")

    def le_float(self, mensagem: str) -> float:
        while True:
            try:
                valor = float(input(mensagem).replace(",", "."))
                if valor <= 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Valor invalido! Digite um numero maior que zero.")
