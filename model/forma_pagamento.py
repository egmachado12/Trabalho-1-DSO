from abc import ABC, abstractmethod


class FormaPagamento(ABC):
    @abstractmethod
    def descricao(self) -> str:
        pass
