import sys
import pygame
from Interfaces.IControladorEventos import IControladorEventos
from prototipo.Jogo import Jogo

class ControladorEventos(IControladorEventos):

    def __init__(self, jogo: Jogo):
        self.__jogo = jogo

    def checaEventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return