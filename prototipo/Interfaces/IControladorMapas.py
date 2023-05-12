from abc import ABC, abstractmethod

from pygame import Surface

from Interfaces.IMapa import IMapa


class IControladorMapas(ABC):

    @abstractmethod
    def __init__(self):
        self.__mapas = {}

    @property
    def mapas(self):
        return self.__mapas
    
    @abstractmethod
    def inclui_mapa(self, mapa: IMapa):
        pass

    @abstractmethod
    def desenha_mapa(self, id_mapa: str, tela: Surface):
        pass