from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def run(self):
        pass