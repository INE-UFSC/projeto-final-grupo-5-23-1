from abc import ABC, abstractmethod


class IMenu(ABC):

    @abstractmethod
    def abrir():
        pass

    @abstractmethod
    def fechar():
        pass
