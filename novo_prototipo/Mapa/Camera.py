import pygame
from settings import *

class Camera(pygame.sprite.Group):
    def __init__(self, tamanho_mapa):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.__tamanhoPixels = tamanho_mapa * 64

        self.__bordaDireitaCamera = self.__tamanhoPixels - 640
        self.__bordaInferiorCamera = self.__tamanhoPixels - 512

    def calcular_offset(self,jogador):
        # Default
        self.offset.x = jogador.rect.centerx - 1280//2
        self.offset.y = jogador.rect.centery - 768 //2

        # Bordas Horizontais
        if jogador.rect.centerx <= 640:
            self.offset.x += (640 - jogador.rect.centerx) 
        elif jogador.rect.centerx >= self.__bordaDireitaCamera:
            self.offset.x += (self.__bordaDireitaCamera - jogador.rect.centerx)
        
        # Bordas Verticais
        if jogador.rect.centery <= 512:
            self.offset.y += (512 - jogador.rect.centery)
        elif jogador.rect.centery >= self.__bordaInferiorCamera:
            self.offset.y += (self.__bordaInferiorCamera - jogador.rect.centery)
    
    def custom_draw(self, jogador):
        self.calcular_offset(jogador)

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    if hasattr(sprite, 'textura'):
                        self.display_surface.blit(sprite.image, offset_rect, sprite.textura)
                    else:
                        self.display_surface.blit(sprite.image, offset_rect)