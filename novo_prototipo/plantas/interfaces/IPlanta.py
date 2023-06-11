from abc import ABC, abstractmethod

import pygame

class IPlanta(pygame.sprite.Sprite, ABC):

    def __init__(self, nome, pos, grupo):
        super().__init__(grupo)
        self.__nome = nome
        self.__pos = pos

    @property
    def nome(self):
        return self.__nome
    
    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        return

    @abstractmethod
    def update(self):
        pass