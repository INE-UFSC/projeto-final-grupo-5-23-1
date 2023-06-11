from abc import ABC, abstractmethod

import pygame

from novo_prototipo.settings import LAYERS

class IPlanta(pygame.sprite.Sprite, ABC):

    def __init__(self, nome, pos, grupo):
        super().__init__(grupo)
        self.__nome = nome
        self.__pos = pos
        self.__z = LAYERS['Entidades']

    @property
    def nome(self):
        return self.__nome
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def z(self):
         return self.__z    
    
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        return

    @abstractmethod
    def update(self):
        pass