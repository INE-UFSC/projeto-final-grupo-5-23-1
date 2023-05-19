'''
Esta classe "abstrata" é utilizada como interface para a classe UserInterface

Posteriormente UserInterface implementará as operações desta classe
'''
from abc import ABC, abstractmethod
class ObservadorModoDeJogo(ABC):
    @abstractmethod
    def worldSizeChanged(self, worldSize):
        pass
    @abstractmethod
    def showMenuRequested(self):
        pass
    @abstractmethod
    def showGameRequested(self):
        pass
    @abstractmethod
    def quitRequested(self):
        pass