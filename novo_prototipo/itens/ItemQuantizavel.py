from .Item import Item
from abc import abstractmethod

class ItemQuantizavel(Item):
    @abstractmethod
    def __init__(self, nome, preco, caminho_imagem, quantidade):
        super().__init__(nome, preco, caminho_imagem)
        self.__quantidade = quantidade

    def reduz_quantidade(self, quantidade_a_ser_reduzida):
        nova_quantidade = self.__quantidade - quantidade_a_ser_reduzida
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade

    @property
    def quantidade(self):
        return self.__quantidade