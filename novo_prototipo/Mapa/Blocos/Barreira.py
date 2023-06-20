import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao

class Barreira(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__mapa = mapa
        self.__custo = self.definir_custo()
    
    def definir_custo(self):
        if self.__mapa == 'Deserto':
            return 10
        elif self.__mapa == 'Neve':
            return 20
        elif self.__mapa == 'Transporte':
            return 30
        elif self.__mapa == 'Planicie':
            return 50
        elif self.__mapa == 'Caverna':
            return 75
    
    def interagir(self, jogador):
        if jogador.moedas >= self.__custo:
            jogador.set_moedas(jogador.moedas - self.__custo)
            self.observador.notifica_exclui_barreira(self.__mapa)
        else:
            print('Dinheiro insuficiente')
    
    @property
    def mapa(self):
        return self.__mapa