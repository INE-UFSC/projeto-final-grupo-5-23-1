import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao

class TerraArada(BlocoComInteracao):

    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x, y, largura, altura, observador)

    def interagir(self, item):
        pass

    def desenhar(self, tela):
        pygame.draw.rect(tela, (155,118,83), (self.x, self.y, self.largura, self.altura))