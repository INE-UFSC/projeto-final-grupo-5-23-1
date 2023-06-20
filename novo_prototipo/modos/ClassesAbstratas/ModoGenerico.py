from abc import ABC, abstractmethod
'''
Esta classe é uma classe "abstrata" que implementa um "modo de jogo"
podendo ele ser realmente o jogo ou apenas uma tela estática.

Esta classe é baseada no design pattern de observadores, logo ela
implementa multiplos métodos para avisar seus observadores das
suas devidas ações
'''
class ModoGenerico(ABC):
    def __init__(self):
        self.__observers = []
    def adiciona_observador(self, observer):
        self.__observers.append(observer)
    def notifyWorldSizeChanged(self, worldSize):
        for observer in self.__observers:
            observer.worldSizeChanged(worldSize)
    def notifyShowMenuRequested(self):
        for observer in self.__observers:
            observer.showMenuRequested()
    def notifyShowGameRequested(self):
        for observer in self.__observers:
            observer.showGameRequested()
    def notifyQuitRequested(self):
        for observer in self.__observers:
            observer.quitRequested()
    def notifica_desativa_menu_principal(self):
        for observer in self.__observers:
            observer.desativa_menu_principal()
    def notifica_aumenta_volume(self):
        for observer in self.__observers:
            observer.aumenta_volume()
    def notifica_baixa_volume(self):
        for observer in self.__observers:
            observer.baixa_volume()
    @property
    def observadores(self):
        return self.__observers
    
    @abstractmethod
    def checa_eventos(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def render(self, window):
        pass