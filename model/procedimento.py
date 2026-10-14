from model.profissional import Profissional


class Procedimento:
    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self.__descricao = None
        self.descricao = descricao
        self.__custo = None
        self.custo = custo
        self.__profissional = None
        self.profissional = profissional

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def custo(self) -> float:
        return self.__custo

    @custo.setter
    def custo(self, custo: float):
        if isinstance(custo, (int,float)):
            self.__custo = float(custo)

    @property
    def profissional(self) -> Profissional:
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if isinstance(profissional, Profissional):
            self.__profissional = profissional

    