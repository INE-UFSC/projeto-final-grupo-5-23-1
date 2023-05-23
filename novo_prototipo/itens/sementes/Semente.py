from itens.ItemQuantizavel import ItemQuantizavel
from abc import abstractmethod

class Semente(ItemQuantizavel):
    @abstractmethod
    def __init__(self, nome, quantidade):
        super().__init__(nome, quantidade)
