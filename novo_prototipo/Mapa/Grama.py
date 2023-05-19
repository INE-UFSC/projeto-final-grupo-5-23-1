import pygame
from Mapa.Bloco import Bloco

class BlocoDeGrama(Bloco):
    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, (0, 64, 0), (self.x, self.y, self.largura, self.altura))