import pygame
from Mapa.Blocos.Bloco import Bloco

class Agua(Bloco):
    def __init__(self,x,y,largura,altura, observador):
        super().__init__(x,y,largura,altura, observador, True)
        self.__image = pygame.Surface((self.largura,self.altura))
        self.__image.fill((0,0,255))
        self.__rect = self.__image.get_rect(topleft= (self.x,self.y))

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    @property
    def rect(self):
        return self.__rect

