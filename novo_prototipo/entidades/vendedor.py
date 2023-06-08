import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao

# Vendedor temporariamente um bloco para MVP

class Vendedor(BlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador, True)
        self.__image = pygame.Surface((64,64))
        self.__image.fill((120,120,120))
        self.__rect = self.__image.get_rect(topleft= pos)

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    def interagir(self, item):
        print('Abre MenuVendas')

    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
