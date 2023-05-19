import pygame
from Bloco import Bloco

class BlocoDeGrama:
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
    
    def desenharGrama(self, tela):
        pygame.draw.rect(tela, (0, 64, 0), (self.x, self.y, self.largura, self.altura))