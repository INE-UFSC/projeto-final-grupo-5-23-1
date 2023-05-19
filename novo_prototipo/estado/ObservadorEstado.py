from abc import ABC, abstractmethod
class ObservadorEstado(ABC):
    
    @abstractmethod
    def algum_metodo(self):
        pass