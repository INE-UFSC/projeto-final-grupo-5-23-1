import pygame
from settings import *
from abc import ABC, abstractmethod


class IBloco(ABC, pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, observador, colisao=False):
        super().__init__(groups)
        self.__image = surf
        self.__rect = self.__image.get_rect(topleft=pos)
        self.__observador = observador
        self.__colisao = colisao
        self.__z = LAYERS['blocos']

        self.__pos = pos
        self.__surf = surf

    @property
    def observador(self):
        return self.__observador
    
    @property
    def posicao_matriz(self):
        posicao_matriz = [self.rect.x, self.rect.y]
        for index, posicao in enumerate(posicao_matriz):
                posicao_matriz[index] = int((posicao // 64))
        return posicao_matriz

    @property
    def colisao(self):
        return self.__colisao

    @property
    def image(self):
         return self.__image
    
    @property
    def rect(self):
         return self.__rect

    @property
    def pos(self):
         return self.__pos
    
    @property
    def surf(self):
         return self.__surf
    
    @property
    def z(self):
         return self.__z
    
    @z.setter
    def z(self, z):
         self.__z = z
    
    @image.setter
    def image(self, image):
         self.__image = image
        
    @rect.setter
    def rect(self, rect):
         self.__rect = rect