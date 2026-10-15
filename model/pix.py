from model.forma_pagamento import FormaPagamento


class Pix(FormaPagamento):
    def __init__(self, cpf_pagador: str):
        self.__cpf_pagador = None
        self.cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self) -> str:
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        if isinstance(cpf_pagador, str):
            self.__cpf_pagador = cpf_pagador


    def descricao(self) -> str:
        return f"Pix-{self.cpf_pagador}"

