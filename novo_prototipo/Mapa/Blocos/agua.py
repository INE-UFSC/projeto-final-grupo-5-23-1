import pygame
from Mapa.Blocos.Bloco import Bloco

class Agua(Bloco):
    def __init__(self,x,y,largura,altura, observador):
        super().__init__(x,y,largura,altura, observador)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (0,0,255), (self.x, self.y, self.largura, self.altura))

