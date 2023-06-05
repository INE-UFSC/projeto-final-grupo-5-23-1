
import pygame

class TrilhaSonora:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./novo_prototipo/trilha/musica_mapa_inicial.mp3')

    def tocar(self):
        pygame.mixer.music.play(-1)

    def parar(self):
        pygame.mixer.music.stop()
