from abc import ABC, abstractmethod


class MenuGenerico(ABC):

    def __init__(self):
        self.__observadores = []
    
    def adiciona_observador(self, observador):
        self.__observadores.append(observador)

    def notifica_desativa_menu(self):
        for observador in self.__observadores:
            observador.desativa_menu()

    @property
    def observadores(self):
        return self.__observadores

    @abstractmethod
    def checa_eventos(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def render(self, window):
        pass