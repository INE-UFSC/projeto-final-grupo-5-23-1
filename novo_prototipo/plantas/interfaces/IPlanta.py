from abc import ABC, abstractmethod

import pygame
from settings import *

class IPlanta(pygame.sprite.Sprite, ABC):

    def __init__(self, nome, pos, grupo):
        super().__init__(grupo)
        self.__nome = nome
        self.__pos = pos
        self.__observadores = []
        self.__em_crescimento = True
        self.__z = LAYERS['main']

    @property
    def nome(self):
        return self.__nome
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def em_crescimento(self):
        return self.__em_crescimento
    
    @em_crescimento.setter
    def em_crescimento(self, em_crescimento: bool):
        if isinstance(em_crescimento, bool):
            self.__em_crescimento = em_crescimento
    
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        return
    
    @property
    def observadores(self):
        return self.__observadores
    
    def adiciona_observador(self, observador):
        self.observadores.append(observador)

    def notifica_exclui_planta(self):
        for observador in self.__observadores:
            observador.excluir_planta()
    
    @property
    def z(self):
        return self.__z

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def interagir(self, jogador):
        pass