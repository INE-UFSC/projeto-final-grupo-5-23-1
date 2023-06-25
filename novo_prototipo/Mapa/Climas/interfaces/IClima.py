from abc import ABC, abstractmethod


class IClima(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.__mapa = None
        self.__observadores = []
    
    @property
    def observadores(self):
        return self.__observadores

    @property
    def mapa(self):
        return self.__mapa

    @mapa.setter
    def mapa(self, mapa):
        self.__mapa = mapa
        return

    def adiciona_observador(self, observador):
        self.observadores.append(observador)
        return

    def notifica_atualiza_clima(self):
        for observador in self.__observadores:
            observador.atualiza_clima(self.__mapa)