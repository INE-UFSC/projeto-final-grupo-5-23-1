from pygame import Surface
import pygame

class Bloco:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def desenhar(self, tela: Surface):
        pygame.draw.rect(tela, (0, 255, 0), (self.x, self.y, self.largura, self.altura))