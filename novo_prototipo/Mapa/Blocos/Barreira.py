import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao

class Barreira(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__mapa = mapa
    
    def interagir(self, jogador):
        if jogador.moedas >= 10:
            jogador.set_moedas(jogador.moedas - 10)
            self.observador.notifica_exclui_barreira(self.__mapa)
    
    @property
    def mapa(self):
        return self.__mapa