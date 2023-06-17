from entidades.jogador.jogador import Jogador
from pytmx.util_pygame import load_pygame
from Mapa.Blocos.Grama import BlocoDeGrama
from Mapa.Blocos.agua import Agua
from Mapa.Blocos.Parede import Parede
from Mapa.Blocos.Transporte import Transporte
from Mapa.interfaces.IMapa import IMapa
import pygame

class MapaDeserto(IMapa):
    def __init__(self, observador):
        super().__init__(observador)
        self.__id = 'Deserto'
    
    @property
    def id(self):
        return self.__id
    
    def construir_blocos(self):
        tmx_data = load_pygame('novo_prototipo/Mapa/Mapas/deserto.tmx')
        
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
            
            if layer.name == 'TpTransporte':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Transporte')
                    self.blocos[y][x] = bloco

            if layer.name == 'TpFloresta':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Floresta')
                    self.blocos[y][x] = bloco
            
            if layer.name == 'TpPlanicie':
                for x, y, surf in layer.tiles():
                    pos = (x*64, y*64)
                    bloco = Transporte(pos= pos, surf= surf, groups= [self.grupoAll, self.grupoBlocos], observador= self, mapa='Planicie')
                    self.blocos[y][x] = bloco

            if layer.name == 'Spawns':
                for obj in layer:
                    self.spawns[obj.name] = pygame.math.Vector2(obj.x, obj.y)
                    
    
    def adiciona_entidades(self):
        self.entidades.append(Jogador(self.spawns['Default'], [self.grupoAll, self.grupoJogador]))