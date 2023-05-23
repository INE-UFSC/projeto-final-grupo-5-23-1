from abc import ABC, abstractmethod

class Item(ABC):

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome