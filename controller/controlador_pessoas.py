from exceptions.cpf_duplicado_exception import CpfDuplicadoException
from exceptions.pessoa_nao_encontrada_exception import PessoaNaoEncontradaException
from model.paciente import Paciente
from model.profissional import Profissional
from view.tela_pessoa import TelaPessoa


class ControladorPessoas:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa()
        self.__pessoas = []

    @property
    def pessoas(self) -> list:
        return self.__pessoas

    # ---------- Buscas (usadas tambem pelos outros controladores) ----------

    def pega_pessoa_por_cpf(self, cpf: str):
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                return pessoa
        raise PessoaNaoEncontradaException(cpf)

    def pega_paciente_por_cpf(self, cpf: str) -> Paciente:
        pessoa = self.pega_pessoa_por_cpf(cpf)
        if not isinstance(pessoa, Paciente):
            raise PessoaNaoEncontradaException(cpf)
        return pessoa

    def pega_profissional_por_cpf(self, cpf: str) -> Profissional:
        pessoa = self.pega_pessoa_por_cpf(cpf)
        if not isinstance(pessoa, Profissional):
            raise PessoaNaoEncontradaException(cpf)
        return pessoa

    def __verifica_cpf_livre(self, cpf: str):
        for pessoa in self.__pessoas:
            if pessoa.cpf == cpf:
                raise CpfDuplicadoException(cpf)

    # ---------- Inclusao, alteracao, exclusao e listagem ----------

    def incluir_paciente(self):
        dados = self.__tela_pessoa.pega_dados_paciente()
        try:
            self.__verifica_cpf_livre(dados["cpf"])
            paciente = Paciente(dados["nome"], dados["celular"],
                                dados["cpf"], dados["data_nascimento"])
            self.__pessoas.append(paciente)
            self.__tela_pessoa.mostra_mensagem("Paciente cadastrado com sucesso!")
        except CpfDuplicadoException as erro:
            self.__tela_pessoa.mostra_mensagem(str(erro))

    def incluir_profissional(self):
        dados = self.__tela_pessoa.pega_dados_profissional()
        try:
            self.__verifica_cpf_livre(dados["cpf"])
            profissional = Profissional(dados["nome"], dados["celular"], dados["cpf"],
                                        dados["especialidade"],
                                        dados["registro_profissional"])
            self.__pessoas.append(profissional)
            self.__tela_pessoa.mostra_mensagem("Profissional cadastrado com sucesso!")
        except CpfDuplicadoException as erro:
            self.__tela_pessoa.mostra_mensagem(str(erro))

    def alterar(self):
        if not self.__tem_pessoas():
            return
        self.listar()
        try:
            pessoa = self.pega_pessoa_por_cpf(self.__tela_pessoa.seleciona_cpf())
            if isinstance(pessoa, Paciente):
                dados = self.__tela_pessoa.pega_dados_paciente(alterando=True)
                pessoa.data_nascimento = dados["data_nascimento"]
            else:
                dados = self.__tela_pessoa.pega_dados_profissional(alterando=True)
                pessoa.especialidade = dados["especialidade"]
                pessoa.registro_profissional = dados["registro_profissional"]
            pessoa.nome = dados["nome"]
            pessoa.celular = dados["celular"]
            self.__tela_pessoa.mostra_mensagem("Dados alterados com sucesso!")
        except PessoaNaoEncontradaException as erro:
            self.__tela_pessoa.mostra_mensagem(str(erro))

    def excluir(self):
        if not self.__tem_pessoas():
            return
        self.listar()
        try:
            pessoa = self.pega_pessoa_por_cpf(self.__tela_pessoa.seleciona_cpf())
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa excluida com sucesso!")
        except PessoaNaoEncontradaException as erro:
            self.__tela_pessoa.mostra_mensagem(str(erro))

    def listar(self):
        if not self.__tem_pessoas():
            return
        for pessoa in self.__pessoas:
            dados = {"tipo": "Paciente" if isinstance(pessoa, Paciente) else "Profissional",
                     "nome": pessoa.nome,
                     "celular": pessoa.celular,
                     "cpf": pessoa.cpf}
            if isinstance(pessoa, Paciente):
                dados["data_nascimento"] = pessoa.data_nascimento.strftime("%d/%m/%Y")
                dados["idade"] = pessoa.idade()
            else:
                dados["especialidade"] = pessoa.especialidade
                dados["registro_profissional"] = pessoa.registro_profissional
            self.__tela_pessoa.mostra_pessoa(dados)

    def __tem_pessoas(self) -> bool:
        if not self.__pessoas:
            self.__tela_pessoa.mostra_mensagem("Nenhuma pessoa cadastrada.")
            return False
        return True

    # ---------- Menu ----------

    def abre_tela(self):
        opcoes = {
            1: self.incluir_paciente,
            2: self.incluir_profissional,
            3: self.alterar,
            4: self.excluir,
            5: self.listar,
        }
        while True:
            opcao = self.__tela_pessoa.tela_opcoes()
            if opcao == 0:
                return
            opcoes[opcao]()
