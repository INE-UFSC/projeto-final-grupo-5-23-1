import pygame
from Mapa.MapaFloresta import MapaFloresta
from Mapa.MapaSavana import MapaSavana
from entidades.jogador.jogador import Jogador

class ControleMapa:
    def __init__(self, observador):
        self.__observador = observador
        self.__mapas = {
            "floresta" : MapaFloresta(self),
            "savana" : MapaSavana(self)
        }

        self.__mapa_atual = self.__mapas['floresta']

    
    def trocar_mapa_atual(self, novo_mapa):
        self.__mapa_atual = self.__mapas[novo_mapa]
        self.observador.set_jogador(self.mapa_atual.jogador)


    @property
    def observador(self):
        return self.__observador
    
    @property
    def mapas(self):
        return self.__mapas
    
    @property
    def mapa_atual(self):
        return self.__mapa_atual
