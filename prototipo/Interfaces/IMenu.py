from abc import ABC, abstractmethod


class IMenu(ABC):

    #[TODO] - Implementar contrutor de janela/tela

    @abstractmethod
    def __init__(self):
        self.__janela

    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def fechar(self):
        pass
