from itens.ItemQuantizavel import ItemQuantizavel
from abc import abstractmethod

from plantas.interfaces.IPlanta import IPlanta

class ISemente(ItemQuantizavel):
    @abstractmethod
    def __init__(self, nome, preco, caminho_imagem, quantidade):
        super().__init__(nome, preco, caminho_imagem, quantidade)

    @abstractmethod
    def constroi_planta(self) -> IPlanta:
        pass
