import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao
from menus.MenuDesbloqueio import MenuDesbloqueio

class Barreira(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__mapa = mapa
        self.__custo = self.definir_custo()
    
    def definir_custo(self):
        if self.__mapa == 'Deserto':
            return 50
        elif self.__mapa == 'Neve':
            return 75
        elif self.__mapa == 'Transporte':
            return 200
        elif self.__mapa == 'Planicie':
            return 100
        elif self.__mapa == 'Caverna':
            return 150
    
    def interagir(self, jogador):
        self.observador.notifica_ativa_menu(MenuDesbloqueio(self, jogador))
    
    @property
    def mapa(self):
        return self.__mapa
    
    @property
    def custo(self):
        return self.__custo