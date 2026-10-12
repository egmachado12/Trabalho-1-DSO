from exceptions.clinica_duplicada_exception import ClinicaDuplicadaException
from exceptions.clinica_nao_encontrada_exception import ClinicaNaoEncontradaException
from exceptions.pessoa_nao_encontrada_exception import PessoaNaoEncontradaException
from model.clinica import Clinica
from view.tela_clinica import TelaClinica


class ControladorClinicas:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_clinica = TelaClinica()
        self.__clinicas = []

    @property
    def clinicas(self) -> list:
        return self.__clinicas

    # ---------- Busca (usada tambem pelos outros controladores) ----------

    def pega_clinica_por_nome(self, nome: str) -> Clinica:
        for clinica in self.__clinicas:
            if clinica.nome.lower() == nome.lower():
                return clinica
        raise ClinicaNaoEncontradaException(nome)

    def __verifica_nome_livre(self, nome: str):
        for clinica in self.__clinicas:
            if clinica.nome.lower() == nome.lower():
                raise ClinicaDuplicadaException(nome)

    # ---------- Inclusao, alteracao, exclusao e listagem ----------

    def incluir(self):
        dados = self.__tela_clinica.pega_dados_clinica()
        try:
            self.__verifica_nome_livre(dados["nome"])
            clinica = Clinica(dados["nome"], dados["cidade"], dados["descricao"],
                              dados["hora_abertura"], dados["hora_fechamento"])
            self.__clinicas.append(clinica)
            self.__tela_clinica.mostra_mensagem("Clinica cadastrada com sucesso!")
        except ClinicaDuplicadaException as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def alterar(self):
        if not self.__tem_clinicas():
            return
        self.listar()
        try:
            clinica = self.pega_clinica_por_nome(self.__tela_clinica.seleciona_clinica())
            dados = self.__tela_clinica.pega_dados_clinica(alterando=True)
            clinica.cidade = dados["cidade"]
            clinica.descricao = dados["descricao"]
            clinica.hora_abertura = dados["hora_abertura"]
            clinica.hora_fechamento = dados["hora_fechamento"]
            self.__tela_clinica.mostra_mensagem("Clinica alterada com sucesso!")
        except ClinicaNaoEncontradaException as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def excluir(self):
        if not self.__tem_clinicas():
            return
        self.listar()
        try:
            clinica = self.pega_clinica_por_nome(self.__tela_clinica.seleciona_clinica())
            self.__clinicas.remove(clinica)
            self.__tela_clinica.mostra_mensagem("Clinica excluida com sucesso!")
        except ClinicaNaoEncontradaException as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def listar(self):
        if not self.__tem_clinicas():
            return
        for clinica in self.__clinicas:
            nomes_profissionais = [p.nome for p in clinica.profissionais]
            self.__tela_clinica.mostra_clinica({
                "nome": clinica.nome,
                "cidade": clinica.cidade,
                "descricao": clinica.descricao,
                "funcionamento": f"{clinica.hora_abertura.strftime('%H:%M')} "
                                 f"as {clinica.hora_fechamento.strftime('%H:%M')}",
                "profissionais": ", ".join(nomes_profissionais) or "nenhum",
            })

    # ---------- Profissionais da clinica (agregacao) ----------

    def adicionar_profissional(self):
        if not self.__tem_clinicas():
            return
        self.listar()
        try:
            clinica = self.pega_clinica_por_nome(self.__tela_clinica.seleciona_clinica())
            cpf = self.__tela_clinica.seleciona_cpf_profissional()
            controlador_pessoas = self.__controlador_sistema.controlador_pessoas
            profissional = controlador_pessoas.pega_profissional_por_cpf(cpf)
            clinica.adicionar_profissional(profissional)
            self.__tela_clinica.mostra_mensagem(
                f"{profissional.nome} agora atende na clinica {clinica.nome}.")
        except (ClinicaNaoEncontradaException, PessoaNaoEncontradaException) as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def remover_profissional(self):
        if not self.__tem_clinicas():
            return
        self.listar()
        try:
            clinica = self.pega_clinica_por_nome(self.__tela_clinica.seleciona_clinica())
            cpf = self.__tela_clinica.seleciona_cpf_profissional()
            controlador_pessoas = self.__controlador_sistema.controlador_pessoas
            profissional = controlador_pessoas.pega_profissional_por_cpf(cpf)
            if profissional not in clinica.profissionais:
                self.__tela_clinica.mostra_mensagem(
                    "Esse profissional nao atende nessa clinica.")
                return
            clinica.remover_profissional(profissional)
            self.__tela_clinica.mostra_mensagem("Profissional removido da clinica.")
        except (ClinicaNaoEncontradaException, PessoaNaoEncontradaException) as erro:
            self.__tela_clinica.mostra_mensagem(str(erro))

    def __tem_clinicas(self) -> bool:
        if not self.__clinicas:
            self.__tela_clinica.mostra_mensagem("Nenhuma clinica cadastrada.")
            return False
        return True

    # ---------- Menu ----------

    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar,
            5: self.adicionar_profissional,
            6: self.remover_profissional,
        }
        while True:
            opcao = self.__tela_clinica.tela_opcoes()
            if opcao == 0:
                return
            opcoes[opcao]()
