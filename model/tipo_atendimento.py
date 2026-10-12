class TipoAtendimento:
    def __init__(self, nome: str, descricao: str):
        self.__nome = None
        self.__descricao = None
        self.nome = nome
        self.descricao = descricao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
