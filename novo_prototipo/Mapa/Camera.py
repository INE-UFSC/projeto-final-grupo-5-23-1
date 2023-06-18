import pygame
from settings import *

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
    
    def custom_draw(self, jogador):
        self.offset.x = jogador.rect.centerx - 1280//2
        self.offset.y = jogador.rect.centery - 768//2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    if hasattr(sprite, 'textura'):
                        self.display_surface.blit(sprite.image, offset_rect, sprite.textura)
                    else:
                        self.display_surface.blit(sprite.image, offset_rect)