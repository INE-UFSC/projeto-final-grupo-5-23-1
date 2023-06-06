import pygame
from Mapa.Blocos.Bloco import Bloco

class Caminho(Bloco):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)

    def desenhar(self, tela):
        pass