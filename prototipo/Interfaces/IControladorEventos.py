from abc import ABC, abstractmethod


class IControladorEventos(ABC):

    @abstractmethod
    def checa_eventos(self):
        pass