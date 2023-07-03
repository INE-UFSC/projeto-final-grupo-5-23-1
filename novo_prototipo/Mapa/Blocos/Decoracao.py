import pygame
from settings import *

class Decoracao(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft= pos)
        self.z = LAYERS['main']