import sys
import pygame
from Interfaces.IControladorEventos import IControladorEventos

class ControladorEventos(IControladorEventos):

    def __init__(self):
        return

    def checa_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        return