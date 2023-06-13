import pygame
from Mapa.Blocos.interfaces.IBlocoComInteracao import IBlocoComInteracao

class Transporte(IBlocoComInteracao):
    def __init__(self, pos, surf, groups, observador, mapa):
        super().__init__(pos, surf, groups, observador, True)
        self.__groups = groups
        self.__mapa = mapa
    
    def interagir(self, jogador):
        self.observador.notifica_troca_mapa(self.__mapa)
        
    def desenhar(self, tela):
        pass