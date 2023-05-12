from abc import ABC, abstractmethod

from pygame import Surface

class IMapa(ABC):

    @abstractmethod
    def __init__(self):
        self.__blocos = []

    @abstractmethod
    def construir_blocos(self):
        pass
    
    @abstractmethod
    def desenhar(self, tela: Surface):
        pass