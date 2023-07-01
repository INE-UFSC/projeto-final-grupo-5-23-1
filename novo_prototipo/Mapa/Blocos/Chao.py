import pygame
from Mapa.Blocos.interfaces.IBloco import IBloco

class Chao(IBloco):
    def __init__(self, pos, surf, groups, observador, manual=False):
        super().__init__(pos, surf, groups, observador)
        self.__manual = manual

        if self.__manual:
            self.image = pygame.image.load('novo_prototipo/Mapa/Mapas/Tilesets/tileset.png')
            self.rect = self.image.get_rect(topleft= pos)
            self.textura = self.definir_textura()
    
    def definir_textura(self):
        if self.observador.id == 'Transporte':
            return (0,128,64,64)
        if self.observador.id == 'Deserto':
            return (576,128,64,64)

    def draw(self, tela):
        if self.__manual:
            tela.blit(self.image, self.rect, self.textura)
        else:
            super().draw()

    def desenhar(self, tela):
        pass
