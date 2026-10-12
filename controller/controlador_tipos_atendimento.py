from exceptions.tipo_atendimento_duplicado_exception import TipoAtendimentoDuplicadoException
from exceptions.tipo_atendimento_nao_encontrado_exception import (
    TipoAtendimentoNaoEncontradoException,
)
from model.tipo_atendimento import TipoAtendimento
from view.tela_tipo_atendimento import TelaTipoAtendimento


class ControladorTiposAtendimento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_tipo = TelaTipoAtendimento()
        self.__tipos = []

    @property
    def tipos(self) -> list:
        return self.__tipos

    # ---------- Busca (usada tambem pelos outros controladores) ----------

    def pega_tipo_por_nome(self, nome: str) -> TipoAtendimento:
        for tipo in self.__tipos:
            if tipo.nome.lower() == nome.lower():
                return tipo
        raise TipoAtendimentoNaoEncontradoException(nome)

    def __verifica_nome_livre(self, nome: str):
        for tipo in self.__tipos:
            if tipo.nome.lower() == nome.lower():
                raise TipoAtendimentoDuplicadoException(nome)

    # ---------- Inclusao, alteracao, exclusao e listagem ----------

    def incluir(self):
        dados = self.__tela_tipo.pega_dados_tipo()
        try:
            self.__verifica_nome_livre(dados["nome"])
            self.__tipos.append(TipoAtendimento(dados["nome"], dados["descricao"]))
            self.__tela_tipo.mostra_mensagem("Tipo de atendimento cadastrado com sucesso!")
        except TipoAtendimentoDuplicadoException as erro:
            self.__tela_tipo.mostra_mensagem(str(erro))

    def alterar(self):
        if not self.__tem_tipos():
            return
        self.listar()
        try:
            tipo = self.pega_tipo_por_nome(self.__tela_tipo.seleciona_tipo())
            dados = self.__tela_tipo.pega_dados_tipo(alterando=True)
            tipo.descricao = dados["descricao"]
            self.__tela_tipo.mostra_mensagem("Tipo de atendimento alterado com sucesso!")
        except TipoAtendimentoNaoEncontradoException as erro:
            self.__tela_tipo.mostra_mensagem(str(erro))

    def excluir(self):
        if not self.__tem_tipos():
            return
        self.listar()
        try:
            tipo = self.pega_tipo_por_nome(self.__tela_tipo.seleciona_tipo())
            self.__tipos.remove(tipo)
            self.__tela_tipo.mostra_mensagem("Tipo de atendimento excluido com sucesso!")
        except TipoAtendimentoNaoEncontradoException as erro:
            self.__tela_tipo.mostra_mensagem(str(erro))

    def listar(self):
        if not self.__tem_tipos():
            return
        for tipo in self.__tipos:
            self.__tela_tipo.mostra_tipo({"nome": tipo.nome, "descricao": tipo.descricao})

    def __tem_tipos(self) -> bool:
        if not self.__tipos:
            self.__tela_tipo.mostra_mensagem("Nenhum tipo de atendimento cadastrado.")
            return False
        return True

    # ---------- Menu ----------

    def abre_tela(self):
        opcoes = {
            1: self.incluir,
            2: self.alterar,
            3: self.excluir,
            4: self.listar,
        }
        while True:
            opcao = self.__tela_tipo.tela_opcoes()
            if opcao == 0:
                return
            opcoes[opcao]()
