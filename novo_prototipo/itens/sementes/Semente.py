from itens.ItemQuantizavel import ItemQuantizavel
from abc import abstractmethod

class Semente(ItemQuantizavel):
    @abstractmethod
    def __init__(self, nome, preco, caminho_imagem, quantidade):
        super().__init__(nome, preco, caminho_imagem, quantidade)
