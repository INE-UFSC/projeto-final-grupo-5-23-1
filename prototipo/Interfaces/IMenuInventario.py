
from abc import abstractmethod

from Interfaces.IMenu import IMenu

    #[TODO] - Implementar base para o inventário

class IMenuInventario(IMenu):

    @abstractmethod
    def __init__(self):
        self.__itens

    
    