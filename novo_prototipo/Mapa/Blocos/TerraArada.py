import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from itens.sementes.ISemente import ISemente
from plantas.interfaces.IPlanta import IPlanta

class TerraArada(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador):
        super().__init__(pos, surf, groups, observador)
        self.__image = pygame.Surface((64,64))
        self.__image.fill((160,82,45))
        self.__rect = self.__image.get_rect(topleft= pos)
        self.__planta = None

    def adiciona_planta(self, planta: IPlanta):
        if isinstance(planta, IPlanta):
            self.__planta = planta

    def notifica_plantar(self, semente: ISemente):
        if isinstance(semente, ISemente):
            self.observador.plantar(self.posicao_matriz[0], self.posicao_matriz[1], semente)

    def interagir(self, jogador):
        if self.__planta == None:
            if isinstance(jogador.item_atual, ISemente):
                self.notifica_plantar(jogador.item_atual)

    def desenhar(self, tela):
        tela.blit(self.__image, self.__rect)
