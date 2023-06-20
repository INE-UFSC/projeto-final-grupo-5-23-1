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
        self.__regada = False
        self.__z = LAYERS['main']

        self.__taxa_de_crescimento = 0
        self.__taxa_de_crescimento_base = 0
        self.__progresso_crescimento = 0

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

    @property
    def progresso_crescimento(self):
        return self.__progresso_crescimento
    
    @progresso_crescimento.setter
    def progresso_crescimento(self, progresso_crescimento):
        self.__progresso_crescimento = progresso_crescimento
    
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
        return
    
    @property
    def observadores(self):
        return self.__observadores
    
    @property
    def regada(self):
        return self.__regada
    
    @regada.setter
    def regada(self, regada: bool):
        self.__regada = regada

    @property
    def taxa_de_crescimento(self):
        return self.__taxa_de_crescimento

    @taxa_de_crescimento.setter
    def taxa_de_crescimento(self, nova_taxa_de_crescimento):
        self.__taxa_de_crescimento = nova_taxa_de_crescimento

    @property
    def taxa_de_crescimento_base(self):
        return self.__taxa_de_crescimento_base

    @taxa_de_crescimento_base.setter
    def taxa_de_crescimento_base(self, nova_taxa_de_crescimento_base):
        self.__taxa_de_crescimento_base = nova_taxa_de_crescimento_base

    def adiciona_observador(self, observador):
        self.observadores.append(observador)

    def notifica_exclui_planta(self):
        for observador in self.__observadores:
            observador.excluir_planta()
    
    @property
    def z(self):
        return self.__z
    
    @abstractmethod
    def atualiza_taxa_de_crescimento(self):
        pass

    @abstractmethod
    def atualiza_sprite(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def interagir(self, jogador):
        pass