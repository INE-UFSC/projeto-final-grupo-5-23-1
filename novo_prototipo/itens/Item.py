from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome