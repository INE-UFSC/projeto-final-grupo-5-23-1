import pygame
from Mapa.Blocos.Bloco import Bloco

class Parede(Bloco):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador, True)

    def desenhar(self, tela):
        pass
