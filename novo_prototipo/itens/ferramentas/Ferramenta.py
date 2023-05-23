from itens.Item import Item
from abc import abstractmethod

class Ferramenta(Item):
    @abstractmethod
    def __init__(self, nome):
        super().__init__(nome)