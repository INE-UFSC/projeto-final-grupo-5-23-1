from abc import ABC, abstractmethod

from pygame import Surface

from menus.ClassesAbstratas.MenuGenerico import MenuGenerico

class IMapa(ABC):

    @abstractmethod
    def __init__(self):
        self.__blocos = []
        self.__observadores = []
    
    @property
    def observadores(self):
        return self.__observadores
    
    def adiciona_observador(self, observador):
        self.__observadores.append(observador)

    def notifica_ativa_menu(self, menu: MenuGenerico):
        for observador in self.__observadores:
            observador.ativa_menu(menu, observador)

    @abstractmethod
    def construir_blocos(self):
        pass
    
    @abstractmethod
    def desenhar(self, tela: Surface):
        pass