class TelaRelatorio:
    def tela_opcoes(self) -> int:
        print()
        print("----- RELATORIOS -----")
        print("1 - Clinicas com maior numero de atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4])

    def mostra_relatorio(self, titulo: str, linhas: list):
        print()
        print(f"=== {titulo} ===")
        for linha in linhas:
            print(linha)

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
