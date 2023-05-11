from abc import ABC, abstractmethod


class IControladorEventos(ABC):

    @abstractmethod
    def checaEventos(self):
        pass