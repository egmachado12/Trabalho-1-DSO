class TelaSistema:
    def tela_opcoes(self) -> int:
        print()
        print("===== SISTEMA DE CLINICAS =====")
        print("1 - Pessoas (pacientes e profissionais)")
        print("2 - Clinicas")
        print("3 - Tipos de atendimento")
        print("4 - Atendimentos")
        print("5 - Pagamentos")
        print("6 - Relatorios")
        print("0 - Sair")
        return self.le_inteiro("Escolha uma opcao: ", [0, 1, 2, 3, 4, 5, 6])

    def le_inteiro(self, mensagem: str, validos: list) -> int:
        while True:
            try:
                valor = int(input(mensagem))
                if valor not in validos:
                    raise ValueError
                return valor
            except ValueError:
                print("Opcao invalida! Digite um dos numeros:", validos)

    def mostra_mensagem(self, mensagem: str):
        print(mensagem)
