from abc import ABC, abstractmethod


class IControladorMapas(ABC):

    @abstractmethod
    def __init__(self):
        self.__mapas = {}
    
    @abstractmethod
    def inclui_mapa(self, mapa):
        pass

    @abstractmethod
    def desenha_mapa(self, id_mapa: str):
        pass