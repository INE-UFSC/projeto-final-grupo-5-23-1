import pygame
from Bloco import Bloco

class Agua(Bloco):
    def __init__(self,x,y,largura,altura):
        super().__init__(x,y,largura,altura)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (0,0,255), (self.x, self.y, self.largura, self.altura))

