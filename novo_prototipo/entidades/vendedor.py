import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao

# Vendedor temporariamente um bloco para MVP

class Vendedor(BlocoComInteracao):
    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x,y,largura,altura,observador, True)
        self.__image = pygame.Surface((self.largura,self.altura))
        self.__image.fill((120,120,120))
        self.__rect = self.__image.get_rect(topleft= (self.x,self.y))

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)

    def interagir(self, item):
        print('abre menu')
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
