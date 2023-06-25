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
        self.__clima = None
        self.__temposBase = None
        self.__temposRegada = None
        self.__temposAtuais = None

        self.__nascimento = pygame.time.get_ticks()

    def atualiza_tempos(self):
        tempo_provisorio = 0
        if self.observadores[0].regada:
            tempo_provisorio = self.temposRegada.copy()
        else:
            tempo_provisorio = self.temposBase.copy()

        multiplicador = self.multiplicador_clima()
        for i, tempo in enumerate(tempo_provisorio):
            tempo_provisorio[i] = tempo * multiplicador
        
        self.temposAtuais = tempo_provisorio
        return

    def calcular_segundos(self):
        return (self.agora - self.nascimento) / 1000

    def update(self):
        if self.em_crescimento:
            self.atualiza_tempos()
            self.atualiza_sprite()

    @property
    def nome(self):
        return self.__nome
    
    @property
    def pos(self):
        return self.__pos
    
    @property
    def em_crescimento(self):
        return self.__em_crescimento
    
    @property
    def nascimento(self):
        return self.__nascimento
    
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
    
    @property
    def regada(self):
        return self.__regada
    
    @regada.setter
    def regada(self, regada: bool):
        self.__regada = regada

    def atualiza_clima(self, clima):
        self.clima = clima

    def adiciona_observador(self, observador):
        self.observadores.append(observador)

    def notifica_exclui_planta(self):
        for observador in self.__observadores:
            observador.excluir_planta()
    
    @property
    def z(self):
        return self.__z
    
    @property
    def clima(self):
        return self.__clima
    
    @property
    def temposAtuais(self):
        return self.__temposAtuais
    
    @temposAtuais.setter
    def temposAtuais(self, temposAtuais):
        self.__temposAtuais = temposAtuais

    @property
    def temposBase(self):
        return self.__temposBase
    
    @temposBase.setter
    def temposBase(self, temposBase):
        self.__temposBase = temposBase

    @property
    def temposRegada(self):
        return self.__temposRegada
    
    @temposRegada.setter
    def temposRegada(self, temposRegada):
        self.__temposRegada = temposRegada
    
    @clima.setter
    def clima(self, clima):
        self.__clima = clima

    @abstractmethod
    def atualiza_sprite(self):
        pass

    @abstractmethod
    def interagir(self, jogador):
        pass

    @abstractmethod
    def multiplicador_clima(self):
        pass