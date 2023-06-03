import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from itens.sementes.Semente import Semente

class TerraArada(BlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
        self.__image = pygame.Surface((64,64))
        self.__image.fill((160,82,45))
        self.__rect = self.__image.get_rect(topleft= pos)
        self.__planta = None

    def adiciona_planta(self, planta):
        self.__planta = planta

    def notifica_plantar(self, item):
        self.observador.plantar(self.posicao_matriz[0], self.posicao_matriz[1], item)

    def interagir(self, item):
        if self.__planta == None:
            if isinstance(item, Semente):
                self.notifica_plantar(item)

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)
