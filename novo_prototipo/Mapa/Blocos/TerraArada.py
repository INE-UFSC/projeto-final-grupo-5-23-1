import pygame
from Mapa.Blocos.BlocoComInteracao import BlocoComInteracao
from itens.sementes.Semente import Semente

class TerraArada(BlocoComInteracao):

    def __init__(self, x, y, largura, altura, observador):
        super().__init__(x, y, largura, altura, observador)
        self.__planta = None

    def adiciona_planta(self, planta):
        self.__planta = planta

    def notifica_plantar(self, item):
        self.observador.plantar(self.posicao_matriz[0], self.posicao_matriz[1], item)

    def interagir(self, jogador):
        if self.__planta == None:
            if isinstance(jogador.item_atual, Semente):
                self.notifica_plantar(jogador.item_atual)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (155,118,83), (self.x, self.y, self.largura, self.altura))
