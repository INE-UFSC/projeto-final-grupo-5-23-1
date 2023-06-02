import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from itens.sementes.Semente import Semente

class TerraArada(BlocoComInteracao):

    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
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
        pygame.draw.rect(tela, (155,118,83), (self.pos.x, self.pos.y, 64, 64))
