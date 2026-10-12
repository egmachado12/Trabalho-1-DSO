class TelaTipoAtendimento:
    def tela_opcoes(self) -> int:
        print()
        print("----- TIPOS DE ATENDIMENTO -----")
        print("1 - Incluir tipo de atendimento")
        print("2 - Alterar tipo de atendimento")
        print("3 - Excluir tipo de atendimento")
        print("4 - Listar tipos de atendimento")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4])

    def pega_dados_tipo(self, alterando: bool = False) -> dict:
        print("--- Dados do tipo de atendimento ---")
        dados = {}
        if not alterando:
            dados["nome"] = self.le_texto("Nome (ex.: Consulta, Exame, Retorno): ")
        dados["descricao"] = self.le_texto("Descricao: ")
        return dados

    def seleciona_tipo(self) -> str:
        return self.le_texto("Digite o nome do tipo de atendimento: ")

    def mostra_tipo(self, dados: dict):
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
