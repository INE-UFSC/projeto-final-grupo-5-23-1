import pygame
from entidades.jogador.jogador import Jogador
from pytmx.util_pygame import load_pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.agua import Agua
from Mapa.Blocos.Parede import Parede
from Mapa.Blocos.Caminho import Caminho
from Mapa.Blocos.Transporte import Transporte
from Mapa.interfaces.IMapa import IMapa

class MapaSavana(IMapa):
    def __init__(self, observador):
        super().__init__(observador)
        self.__id = 'savana'
    
    @property
    def id(self):
        return self.__id
    
    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/savana.tmx')
        
        for layer in tmx_data.layers:
            if layer.name  == 'Fundo':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Agua(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador=self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Parede':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Parede(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Grama':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = BlocoDeGrama(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco

            if layer.name == 'Caminho':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Caminho(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self)
                    self.blocos[y][x] = bloco
            
            if layer.name == 'Transporte':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='floresta')
                    self.blocos[y][x] = bloco

            if layer.name == 'Interacao':
                for obj in layer:
                    if obj.name == 'Spawn':
                        self.__playerSpawnX = obj.x
                        self.__playerSpawnY = obj.y
    
    def adiciona_entidades(self):
        self.entidades.append(Jogador((self.__playerSpawnX, self.__playerSpawnY), [self.grupoAll, self.grupoJogador]))